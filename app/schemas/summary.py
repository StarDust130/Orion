from pydantic import BaseModel


class SummaryResponse(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
