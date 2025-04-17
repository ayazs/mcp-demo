# app/routes/chat.py
from fastapi import APIRouter, Request
from app.services.llm_router import call_model

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    result = await call_model(prompt)
    return {"response": result}

    