from collections import defaultdict

from groq.types.chat import ChatCompletionMessageParam


class MemoryStore:
    CONTEXT_LIMIT = 20

    def __init__(self) -> None:
        self._conversations: dict[
            str,
            list[ChatCompletionMessageParam],
        ] = defaultdict(list)

    def get_messages(
        self,
        conversation_id: str,
    ) -> list[ChatCompletionMessageParam]:
        # Keep the complete conversation stored, but send only recent context
        # to the model so it remembers the latest 20 messages.
        return self._conversations[conversation_id][-self.CONTEXT_LIMIT :]

    def add_message(
        self,
        conversation_id: str,
        message: ChatCompletionMessageParam,
    ) -> None:
        self._conversations[conversation_id].append(message)
