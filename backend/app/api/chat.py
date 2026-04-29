from fastapi import APIRouter
from pydantic import BaseModel
from app.agent.graph import graph
from langchain_core.messages import HumanMessage, SystemMessage
from app.db.database import SessionLocal
from app.db import crud
from datetime import datetime

router = APIRouter()

# Schema for the incoming JSON request from React
class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # 1. PRE-PROCESSING: Get the latest record ID
    # We pass this to the AI so it knows what record is currently 'on screen' for editing
    db = SessionLocal()
    latest = crud.get_latest_interaction(db)
    current_id = latest.id if latest else "None"
    db.close()

    # 2. SYSTEM PROMPT: This defines the AI's personality and constraints
    system_msg = SystemMessage(content=(
        f"You are a medical CRM assistant. Current active ID: {current_id}. "
        "Goal: Use tools to help the user. If you use 'get_product_info_tool', explain results in detail. "
        "Strictly categorize sentiment as 'Positive', 'Neutral', or 'Negative'. "
        "Once a tool provides a result, summarize and STOP. Do not loop."
    ))
    
    # 3. GRAPH EXECUTION: Run the LangGraph workflow
    # We set a recursion_limit of 10 to prevent the AI from talking to itself forever
    initial_state = {"messages": [system_msg, HumanMessage(content=request.message)]}
    result = graph.invoke(initial_state, config={"recursion_limit": 10})
    
    # 4. POST-PROCESSING: Fetch the data again in case a tool modified the DB
    db = SessionLocal()
    fresh_data = crud.get_latest_interaction(db)
    db.close()

    # 5. RESPONSE: Send the AI's text and the updated DB record back to the frontend
    now = datetime.now()
    return {
        "response": result["messages"][-1].content, # The AI's final text summary
        "extracted_data": {
            "hcp_name": fresh_data.hcp_name if fresh_data else "",
            "interaction_type": "Meeting",
            "date": now.strftime("%m/%d/%Y"), # Automatically set current date
            "time": now.strftime("%I:%M %p"), # Automatically set current time
            "topics_discussed": fresh_data.notes if fresh_data else "",
            "sentiment": fresh_data.sentiment if fresh_data else "Neutral"
        }
    }