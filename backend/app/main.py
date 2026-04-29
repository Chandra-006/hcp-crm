"""
Main FastAPI application for the AI-Powered HCP CRM Assistant.

This module initializes the FastAPI app, sets up CORS middleware for frontend communication,
includes API routers, and handles database table creation on startup.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base, create_tables
import os
from app.api.chat import router as chat_router

# This creates the database tables automatically when the app starts
create_tables()

app = FastAPI(title="AI-First CRM HCP Module")

# This allows our React frontend to talk to this Python backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    Root endpoint to check if the backend is running.

    Returns:
        dict: A message indicating the backend status.
    """
    return {"message": "HCP CRM Backend is running!"}

# Include the chat API router with prefix
app.include_router(chat_router, prefix="/api")