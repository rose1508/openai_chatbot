#  AI Chatbot Backend API

This project is a production-ready backend for an AI-powered chatbot built with **FastAPI**, integrated with **OpenAI’s GPT**, and backed by a **PostgreSQL** database. It provides RESTful endpoints to send messages, receive intelligent replies, and view chat history.

##  Features

-  RESTful API with FastAPI
-  GPT-based response generation using OpenAI
-  PostgreSQL database for storing message history
-  Dockerized architecture with `docker-compose`
-  API documentation via Swagger (`/docs`)

##  Project Structure

#   o p e n a i _ c h a t b o t 
 
 ai_chatbot/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── ai_service.py
├── .env
├── requirements.txt
