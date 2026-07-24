from app.llm.providers.base import BaseLLMProvider
from app.schemas.chat import ChatResponse


class ChatService:
    def __init__(self, provider: BaseLLMProvider) -> None:
        self.provider = provider

    async def chat(self, message: str) -> ChatResponse:
        response = await self.provider.chat(message)

        return ChatResponse(response=response)
