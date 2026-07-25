from abc import ABC, abstractmethod

from groq.types.chat import ChatCompletionMessageParam


class BaseLLMProvider(ABC):
    @abstractmethod
    async def chat(
        self,
        history: list[ChatCompletionMessageParam],
        message: str,
    ) -> str:
        pass
