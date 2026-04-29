"""
Database configuration module for the HCP CRM application.

This module sets up the SQLAlchemy engine, session maker, and base class for database operations.
It also provides a dependency for getting database sessions and a function to create tables.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment, with a default for local development
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/hcp_crm")

# Create SQLAlchemy engine for database connection
engine = create_engine(DATABASE_URL)

# Create session maker for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()


def get_db():
    """
    Dependency function to get a database session.

    Yields:
        Session: A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """
    Create all database tables defined in the models.

    This function imports the models to ensure they are registered with the Base metadata,
    then creates all tables in the database.
    """
    from app.models.interaction import Interaction  # noqa: F401
    Base.metadata.create_all(bind=engine)