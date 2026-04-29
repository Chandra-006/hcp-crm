"""
CRUD operations for Interaction model.

This module provides functions to create, read, update, and query Interaction records
in the database using SQLAlchemy.
"""

from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):
    """
    Create a new interaction record in the database.

    Args:
        db (Session): Database session.
        interaction (InteractionCreate): Interaction data to create.

    Returns:
        Interaction: The created interaction object.
    """
    db_interaction = Interaction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction


def get_latest_interaction(db: Session):
    """
    Retrieve the most recently created interaction.

    Args:
        db (Session): Database session.

    Returns:
        Interaction or None: The latest interaction, or None if no interactions exist.
    """
    return db.query(Interaction).order_by(Interaction.id.desc()).first()


def update_interaction(db: Session, interaction_id: int, updates: dict):
    """
    Update an existing interaction with the provided changes.

    Args:
        db (Session): Database session.
        interaction_id (int): ID of the interaction to update.
        updates (dict): Dictionary of fields to update.

    Returns:
        Interaction or None: The updated interaction, or None if not found.
    """
    db_interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if db_interaction:
        for key, value in updates.items():
            setattr(db_interaction, key, value)
        db.commit()
        db.refresh(db_interaction)
    return db_interaction


def get_interactions_by_name(db: Session, hcp_name: str):
    """
    Retrieve all interactions for a specific HCP name (case-insensitive partial match).

    Args:
        db (Session): Database session.
        hcp_name (str): Name of the HCP to search for.

    Returns:
        list[Interaction]: List of matching interactions.
    """
    return db.query(Interaction).filter(
        Interaction.hcp_name.ilike(f"%{hcp_name}%")
    ).all()