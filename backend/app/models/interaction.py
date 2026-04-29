"""
SQLAlchemy model for Interaction entities.

This module defines the Interaction class, which represents a database table for storing
Healthcare Professional (HCP) interaction records.
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.db.database import Base


class Interaction(Base):
    """
    SQLAlchemy model for HCP interactions.

    Attributes:
        id (int): Primary key for the interaction.
        hcp_name (str): Name of the Healthcare Professional.
        hcp_specialty (str): Specialty of the HCP.
        interaction_date (str): Date of the interaction.
        interaction_type (str): Type of interaction (e.g., Meeting).
        location (str): Location where the interaction occurred.
        products_discussed (list): JSON list of products discussed.
        sentiment (str): Sentiment of the interaction (Positive, Neutral, Negative).
        materials_shared (list): JSON list of materials shared.
        follow_up_required (bool): Whether follow-up is required.
        follow_up_date (str): Date for follow-up if required.
        notes (str): Additional notes from the interaction.
        summary (str): Summary of the interaction.
        next_steps (str): Next steps planned.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
    """
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255), nullable=True)
    hcp_specialty = Column(String(255), nullable=True)
    interaction_date = Column(String(50), nullable=True)
    interaction_type = Column(String(100), nullable=True)
    location = Column(String(255), nullable=True)
    products_discussed = Column(JSON, nullable=True, default=list)
    sentiment = Column(String(50), nullable=True)
    materials_shared = Column(JSON, nullable=True, default=list)
    follow_up_required = Column(Boolean, default=False)
    follow_up_date = Column(String(50), nullable=True)
    notes = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    next_steps = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())