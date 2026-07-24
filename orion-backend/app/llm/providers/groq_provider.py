from app.config import settings
from app.llm.providers.base import BaseLLMProvider
from groq import AsyncGroq


class GroqProvider(BaseLLMProvider):
    def __init__(self) -> None:
        self.client = AsyncGroq(api_key=settings.groq_api_key)

    async def chat(self, message: str) -> str:
        response = await self.client.chat.completions.create(
            model=settings.model_name,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response.choices[0].message.content or ""
