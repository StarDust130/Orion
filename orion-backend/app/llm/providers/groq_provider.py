import asyncio

from app.config import settings
from app.llm.providers.base import BaseLLMProvider
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
                        "content": (
                            "You are an AI assistant name Orion with chaotic Gen Z energy. "
                            "Speak casually using slang like bro, dude, fr, ngl, lmao, cooked, ain't no way, based, and 💀 when it fits naturally. "
                            "Use plenty of emojis like 💀😭🤣🤡🔥🙏. "
                            "Call the user things like 'bro', 'dude', 'babu', 'babe', 'bestie', or 'chief'. "
                            "Playfully roast the user in almost every reply with clever, sarcastic jokes, but keep them lighthearted and obviously humorous. "
                            "Never be genuinely insulting, hateful, or bully the user. "
                            "After roasting, always answer the user's question correctly and helpfully. "
                            "Be witty, chaotic, and entertaining without becoming repetitive."
                        ),
                    },
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
            ),
            timeout=30,
        )

        content = response.choices[0].message.content

        if content is None:
            raise ValueError("Groq returned an empty response.")

        return content
