# app/services/llm_router.py
import os
# from langchain_openai import ChatOpenAI  # Make sure you've installed langchain-openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from app.config import load_env

load_env()  # Load env vars

async def call_model(prompt: str) -> str:

    # OpenRouter models
    # model = route_to_openrouter_model("gpt-3.5-turbo")
    model = route_to_openrouter_model("mistralai/mistral-7b-instruct")

    #
    # model = ChatOpenAI(
    #     temperature=0.2,    
    #     model_name="gpt-3.5-turbo",  # or gpt-4
    #     api_key=os.getenv("OPENAI_API_KEY")
    # )

    message = HumanMessage(content=prompt)
    response = model.invoke([message])
    return response.content

def route_to_openrouter_model(model_name: str) -> ChatOpenAI:
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
    return ChatOpenAI(
        model_name=model_name,
        temperature=0.2,
        base_url="https://openrouter.ai/api/v1"
    )