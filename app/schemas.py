from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    user_id: str
    question: str

class ChatResponse(BaseModel):
    answer: str

class ChatHistory(BaseModel):
    id: int
    user_id: str
    question: str
    answer: str
    timestamp: datetime

    class Config:
        orm_mode = True
