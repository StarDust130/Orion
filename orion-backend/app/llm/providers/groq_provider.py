import asyncio

from app.config import settings
from app.llm.providers.base import BaseLLMProvider
from app.prompts.chat import CHAT_SYSTEM_PROMPT
from groq import AsyncGroq


class GroqProvider(BaseLLMProvider):
    def __init__(self) -> None:
        self.client = AsyncGroq(
            api_key=settings.groq_api_key,
        )

    async def chat(self, message: str) -> str:
        response = await asyncio.wait_for(
            self.client.chat.completions.create(
                model=settings.model_name,
                messages=[
                    {
                        "role": "system",
                        "content": CHAT_SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
                temperature=0.7,
            ),
            timeout=30,
        )

        content = response.choices[0].message.content

        if content is None:
            raise ValueError("Groq returned an empty response.")

        return content
