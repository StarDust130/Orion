from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    conversation_id: str = Field(
        min_length=1,
        description="Conversation ID",
    )

    message: str = Field(
        min_length=1,
        max_length=5000,
    )

    @field_validator("conversation_id", "message")
    @classmethod
    def validate_strings(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty.")

        return value


class ChatResponse(BaseModel):
    response: str
