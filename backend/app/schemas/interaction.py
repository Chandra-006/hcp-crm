from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# This defines what the data looks like when saving a new interaction
class InteractionBase(BaseModel):
    hcp_name: Optional[str] = None
    hcp_specialty: Optional[str] = None
    interaction_date: Optional[str] = None
    interaction_type: Optional[str] = None
    location: Optional[str] = None
    products_discussed: List[str] = []
    sentiment: Optional[str] = None
    materials_shared: List[str] = []
    follow_up_required: bool = False
    follow_up_date: Optional[str] = None
    notes: Optional[str] = None
    summary: Optional[str] = None
    next_steps: Optional[str] = None

class InteractionCreate(InteractionBase):
    pass

# This is what the backend sends back to the frontend (includes ID and timestamps)
class Interaction(InteractionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True