from app.core.logging import logger
from app.llm.providers.base import BaseLLMProvider
from app.memory.store import MemoryStore
from app.schemas.chat import ChatResponse


class ChatService:
    def __init__(
        self,
        provider: BaseLLMProvider,
        memory: MemoryStore,
    ) -> None:
        self.provider = provider
        self.memory = memory

    async def chat(
        self,
        conversation_id: str,
        message: str,
    ) -> ChatResponse:
        history = self.memory.get_messages(conversation_id)

        logger.info("Sending request to provider")

        reply = await self.provider.chat(
            history=history,
            message=message,
        )

        logger.info("Provider response received")

        # Save user message
        self.memory.add_message(
            conversation_id,
            {
                "role": "user",
                "content": message,
            },
        )

        # Save assistant reply
        self.memory.add_message(
            conversation_id,
            {
                "role": "assistant",
                "content": reply,
            },
        )

        return ChatResponse(response=reply)