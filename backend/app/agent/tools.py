from langchain_core.tools import tool
from app.db.database import SessionLocal
from app.db import crud
from app.schemas.interaction import InteractionCreate
from typing import Union
import json

@tool
def log_interaction_tool(hcp_name: str, sentiment: str, notes: str):
    """
    TOOL #1: Create a new database entry.
    Triggered when the AI identifies a new meeting report.
    """
    db = SessionLocal()
    try:
        # Convert raw AI strings into a structured Schema object
        interaction_obj = InteractionCreate(hcp_name=hcp_name, sentiment=sentiment, notes=notes)
        # Call CRUD to save into PostgreSQL
        result = crud.create_interaction(db, interaction_obj)
        return f"Successfully logged interaction for {hcp_name} with ID: {result.id}"
    finally:
        db.close() # Always close DB session to prevent memory leaks

@tool
def edit_interaction_tool(interaction_id: Union[int, str], hcp_name: str = None, sentiment: str = None, notes: str = None):
    """
    TOOL #2: Modify an existing record.
    Uses Union[int, str] because LLMs often send numbers as strings.
    """
    db = SessionLocal()
    try:
        target_id = int(interaction_id)
        # Create a dictionary of only the fields the user actually wanted to change
        updates = {k: v for k, v in {"hcp_name": hcp_name, "sentiment": sentiment, "notes": notes}.items() if v is not None}
        result = crud.update_interaction(db, target_id, updates)
        return f"Successfully updated interaction {target_id}" if result else "ID not found."
    finally:
        db.close()

@tool
def get_interaction_history_tool(hcp_name: str):
    """
    TOOL #3: Database Lookup.
    Searches past records so the AI can answer 'What did we talk about last time?'
    """
    db = SessionLocal()
    try:
        history = crud.get_interactions_by_name(db, hcp_name)
        if not history: return f"No previous records found for {hcp_name}."
        # Return as JSON string so the LLM can parse and summarize it
        return json.dumps([{"date": str(h.created_at.date()), "sentiment": h.sentiment, "notes": h.notes} for h in history])
    finally:
        db.close()

@tool
def schedule_follow_up_tool(interaction_id: Union[int, str], date: str):
    """
    TOOL #4: Task Scheduling.
    Updates the follow-up columns in the database for a specific record.
    """
    db = SessionLocal()
    try:
        target_id = int(interaction_id)
        crud.update_interaction(db, target_id, {"follow_up_date": date, "follow_up_required": True})
        return f"Follow-up for record {target_id} scheduled for {date}."
    finally:
        db.close()

@tool
def get_product_info_tool(product_name: str):
    """
    TOOL #5: Knowledge Base / RAG-lite.
    Provides technical data about medicines/products that the AI might not know natively.
    """
    kb = {
        "product x": "Cardiology focus. Reduces cholesterol. Side effects: Mild fatigue.",
        "product y": "Respiratory focus. Treats asthma. Side effects: Dry throat.",
        "b-complex": "Contains 8 vitamins. Converts food to energy and supports brain function.",
        "b-complex tablet": "500mg dose. Used for metabolic support and nervous system health."
    }
    # Standardize input to lowercase to match keys in dictionary
    return kb.get(product_name.lower().strip(), f"No details found for {product_name}.")

# Export all tools so they can be bound to the LangGraph Agent
tools = [log_interaction_tool, edit_interaction_tool, get_interaction_history_tool, schedule_follow_up_tool, get_product_info_tool]