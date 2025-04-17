# app/services/llm_router.py
import os
from langchain_openai import ChatOpenAI  # Make sure you've installed langchain-openai
# from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from app.config import load_env

load_env()  # Load env vars

async def call_model(prompt: str) -> str:
    model = ChatOpenAI(
        temperature=0.2,
        model_name="gpt-3.5-turbo",  # or gpt-4
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    message = HumanMessage(content=prompt)
    response = model.invoke([message])
    return response.content
    