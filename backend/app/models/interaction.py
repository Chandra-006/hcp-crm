from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.db.database import Base

class Interaction(Base):
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