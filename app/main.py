from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
import openai, os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to handle chat requests
@app.post("/chat", response_model=schemas.ChatResponse)
def chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    """
    Handle user chat input, generate a response using GPT, and save the conversation.
    """
    # Generate response using OpenAI GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request.question}]
    )
    answer = response.choices[0].message.content

    # Save the conversation to the database
    crud.save_conversation(db, request.user_id, request.question, answer)

    # Return the generated answer
    return {"answer": answer}

# Route to retrieve conversation history for a user
@app.get("/conversations/{user_id}", response_model=list[schemas.ChatHistory])
def get_history(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all conversations for a specific user.
    """
    return crud.get_conversations(db, user_id)


# Entry point for running the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)