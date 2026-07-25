import asyncio

from app.config import settings
from app.llm.providers.base import BaseLLMProvider
from app.prompts.builder import PromptBuilder
from groq import AsyncGroq


class GroqProvider(BaseLLMProvider):
    def __init__(self) -> None:
        self.client = AsyncGroq(
            api_key=settings.groq_api_key,
        )

    async def chat(self, message: str) -> str:
        messages = PromptBuilder.build_chat_prompt(message)

        response = await asyncio.wait_for(
            self.client.chat.completions.create(
                model=settings.model_name,
                messages=messages,
                temperature=0.7,
            ),
            timeout=30,
        )

        content = response.choices[0].message.content

        if content is None:
            raise ValueError("Groq returned an empty response.")

        return content
