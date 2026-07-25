from app.llm.providers.groq_provider import GroqProvider
from app.services.chat_service import ChatService


def get_chat_service() -> ChatService:
    provider = GroqProvider()
    return ChatService(provider)
