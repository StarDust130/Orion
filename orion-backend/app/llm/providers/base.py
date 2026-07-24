from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    @abstractmethod
    async def chat(self, message: str) -> str:
        """Generate a response from the LLM."""
