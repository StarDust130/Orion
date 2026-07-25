from collections import defaultdict

from groq.types.chat import ChatCompletionMessageParam


class MemoryStore:
    def __init__(self) -> None:
        self._conversations: dict[
            str,
            list[ChatCompletionMessageParam],
        ] = defaultdict(list)

    def get_messages(
        self,
        conversation_id: str,
    ) -> list[ChatCompletionMessageParam]:
        return self._conversations[conversation_id]

    def add_message(
        self,
        conversation_id: str,
        message: ChatCompletionMessageParam,
    ) -> None:
        self._conversations[conversation_id].append(message)
