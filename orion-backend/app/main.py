from app.api.chat import router as chat_router
from app.config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
async def root():
    return {"message": "Welcome to Orion 🚀"}

# Routes 🪝
app.include_router(chat_router)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }
