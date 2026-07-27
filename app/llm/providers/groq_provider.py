import asyncio

from groq import AsyncGroq
from groq.types.chat import ChatCompletionMessage, ChatCompletionMessageParam

from app.config import settings
from app.llm.providers.base import BaseLLMProvider
from app.prompts.builder import PromptBuilder


class GroqProvider(BaseLLMProvider):
    def __init__(self) -> None:
        self.client = AsyncGroq(
            api_key=settings.groq_api_key,
        )

    async def chat(
        self,
        history: list[ChatCompletionMessageParam],
        message: str | None = None,
        tools: list[dict] | None = None,
    ) -> ChatCompletionMessage:
        messages = PromptBuilder.build_chat_prompt(
            history,
            message,
        )

        response = await asyncio.wait_for(
            self.client.chat.completions.create(
                model=settings.model_name,
                messages=messages,
                tools=tools or None,
                tool_choice="auto",
                # response_format={
                #     "type": "json_object", # for json format answer
                # },
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
                top_p=settings.top_p,
                frequency_penalty=settings.frequency_penalty,
                presence_penalty=settings.presence_penalty,
                # stream=True,  # Enable streaming for real-time responses
            ),
            timeout=30,
        )

        return response.choices[0].message
