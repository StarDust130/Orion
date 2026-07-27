from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.config import settings
from app.core.exceptions import global_exception_handler
from app.core.middleware import add_request_id

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

# Middleware  🧵
app.middleware("http")(add_request_id)  # Add Request ID to each request.



@app.get("/")
async def root():
    return {"message": "Welcome to Orion 🚀"}


# Routes 🪝
app.include_router(chat_router)


@app.get("/health")
async def health():
    return {
        "name": settings.app_name,
        "status": "Healthy ✅",
        "version": settings.app_version,
        "environment": settings.environment,
    }


# Exception Handler ( Handle Errors Globally ) 🛠️
app.add_exception_handler(
    Exception,
    global_exception_handler,
)
