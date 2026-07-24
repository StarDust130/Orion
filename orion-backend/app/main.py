from app.config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Orion 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }
