from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

service = ChatService()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return await service.chat(request.message)
