from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
import openai, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

@router.post("/chat", response_model=schemas.ChatResponse)
def chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request.question}]
    )
    answer = response.choices[0].message.content
    crud.save_conversation(db, request.user_id, request.question, answer)
    return {"answer": answer}

@router.get("/conversations/{user_id}", response_model=list[schemas.ChatHistory])
def get_history(user_id: str, db: Session = Depends(get_db)):
    return crud.get_conversations(db, user_id)