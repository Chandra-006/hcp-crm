import os
from typing import TypedDict, Annotated, Sequence
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, SystemMessage
from langgraph.graph import StateGraph, END, add_messages
from langgraph.prebuilt import ToolNode
from app.agent.tools import tools

# 1. Define State
class AgentState(TypedDict):
    # This automatically handles merging new messages into the conversation
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 2. Initialize LLM
llm = ChatGroq(
    temperature=0, 
    model_name="llama-3.3-70b-versatile", 
    groq_api_key=os.getenv("GROQ_API_KEY")
)
llm_with_tools = llm.bind_tools(tools)

# 3. Define Nodes
def call_model(state: AgentState):
    # Add a strong instruction to finish after tool use
    sys_msg = SystemMessage(content="You are a CRM assistant. After using a tool, summarize the result and STOP immediately. Do not call tools in a loop.")
    response = llm_with_tools.invoke([sys_msg] + state["messages"])
    return {"messages": [response]}

# 4. Define Logic for Routing
def router(state: AgentState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END

# 5. Build Workflow
workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))

workflow.set_entry_point("agent")

# The agent decides: go to tools or END
workflow.add_conditional_edges("agent", router)

# After tools are used, it MUST go back to the agent for a final summary
workflow.add_edge("tools", "agent")

graph = workflow.compile()