from app.llm.providers.groq_provider import GroqProvider
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

provider = GroqProvider()
service = ChatService(provider)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await service.chat(request.message)
