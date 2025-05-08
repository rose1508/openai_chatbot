from sqlalchemy.orm import Session
from app import models

def save_conversation(db: Session, user_id: str, question: str, answer: str):
    convo = models.Conversation(user_id=user_id, question=question, answer=answer)
    db.add(convo)
    db.commit()
    db.refresh(convo)
    return convo

def get_conversations(db: Session, user_id: str):
    return db.query(models.Conversation).filter(models.Conversation.user_id == user_id).all()
