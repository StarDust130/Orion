from abc import ABC, abstractmethod

from groq.types.chat import ChatCompletionMessage, ChatCompletionMessageParam


class BaseLLMProvider(ABC):
    @abstractmethod
    async def chat(
        self,
        history: list[ChatCompletionMessageParam],
        message: str | None = None,
        tools: list[dict] | None = None,
    ) -> ChatCompletionMessage:
        pass
