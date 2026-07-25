from app.prompts.chat import CHAT_SYSTEM_PROMPT
from groq.types.chat import ChatCompletionMessageParam


class PromptBuilder:
    @staticmethod
    def build_chat_prompt(message: str) -> list[ChatCompletionMessageParam]:
        return [
            {
                "role": "system",
                "content": CHAT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ]
