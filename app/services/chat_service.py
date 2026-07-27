import json
from typing import cast

from openai.types.chat import ChatCompletionMessageParam

from app.llm.providers.base import BaseLLMProvider
from app.memory.store import MemoryStore
from app.schemas.chat import ChatResponse
from app.tools.manager import ToolManager


class ChatService:
    def __init__(
        self,
        provider: BaseLLMProvider,
        memory: MemoryStore,
        tool_manager: ToolManager,
    ) -> None:
        self.provider = provider
        self.memory = memory
        self.tool_manager = tool_manager

    async def chat(
        self,
        conversation_id: str,
        message: str,
    ) -> ChatResponse:
        self.memory.add_message(
            conversation_id,
            cast(
                ChatCompletionMessageParam,
                {
                    "role": "user",
                    "content": message,
                },
            ),
        )

        assistant_message = await self.provider.chat(
            history=self.memory.get_messages(conversation_id),
            tools=self.tool_manager.schemas(),
        )
        while assistant_message.tool_calls:
            self.memory.add_message(
                conversation_id,
                cast(
                    ChatCompletionMessageParam,
                    assistant_message.model_dump(exclude_none=True),
                ),
            )
            for tool_call in assistant_message.tool_calls:
                result = await self.tool_manager.execute(
                    tool_call.function.name,
                    json.loads(tool_call.function.arguments),
                )
                self.memory.add_message(
                    conversation_id,
                    cast(
                        ChatCompletionMessageParam,
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": str(result),
                        },
                    ),
                )
            assistant_message = await self.provider.chat(
                history=self.memory.get_messages(conversation_id),
                tools=self.tool_manager.schemas(),
            )
        reply = assistant_message.content or ""

        # Save assistant reply
        self.memory.add_message(
            conversation_id,
            cast(
                ChatCompletionMessageParam,
                {
                    "role": "assistant",
                    "content": reply,
                },
            ),
        )

        return ChatResponse(response=reply)
