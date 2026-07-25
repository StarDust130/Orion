from app.core.logging import logger
from app.llm.providers.base import BaseLLMProvider
from app.schemas.chat import ChatResponse


class ChatService:
    def __init__(self, provider: BaseLLMProvider) -> None:
        self.provider = provider

    async def chat(self,conversation_id: str,message: str) -> ChatResponse:
        logger.info("Sending request to provider 😚")
        response = await self.provider.chat(message)
        logger.info("Provider response received 🤭")

        return ChatResponse(response=response)
