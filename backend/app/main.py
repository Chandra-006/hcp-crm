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
    return {"message": "HCP CRM Backend is running!"}

from app.api.chat import router as chat_router
app.include_router(chat_router, prefix="/api")