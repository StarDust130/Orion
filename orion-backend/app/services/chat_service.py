from app.schemas.chat import ChatResponse


class ChatService:
    async def chat(self, message: str) -> ChatResponse:
        return ChatResponse(response=f"You said: {message}")
