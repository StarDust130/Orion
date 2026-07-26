from groq.types.chat import ChatCompletionMessageParam

from app.prompts.chat import CHAT_SYSTEM_PROMPT


class PromptBuilder:
    @staticmethod
    def build_chat_prompt(
        history: list[ChatCompletionMessageParam],
        message: str | None = None,
    ) -> list[ChatCompletionMessageParam]:

        return [
            {
                "role": "system",
                "content": CHAT_SYSTEM_PROMPT,
            },
            *history,
            *([{"role": "user", "content": message}] if message is not None else []),
        ]
