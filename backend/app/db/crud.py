from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate

def create_interaction(db: Session, interaction: InteractionCreate):
    db_interaction = Interaction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_latest_interaction(db: Session):
    return db.query(Interaction).order_by(Interaction.id.desc()).first()

def update_interaction(db: Session, interaction_id: int, updates: dict):
    db_interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if db_interaction:
        for key, value in updates.items():
            setattr(db_interaction, key, value)
        db.commit()
        db.refresh(db_interaction)
    return db_interaction

# --- NEW FUNCTION FOR TOOL #3 ---
def get_interactions_by_name(db: Session, hcp_name: str):
    """Searches the database for all meetings with a specific doctor."""
    return db.query(Interaction).filter(
        Interaction.hcp_name.ilike(f"%{hcp_name}%")
    ).all()