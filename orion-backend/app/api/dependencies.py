from functools import lru_cache

from app.llm.providers.groq_provider import GroqProvider
from app.memory.store import MemoryStore
from app.services.chat_service import ChatService
from app.tools.manager import ToolManager


@lru_cache(maxsize=1)
def get_chat_service() -> ChatService:
    provider = GroqProvider()
    return ChatService(provider, MemoryStore(), ToolManager())
