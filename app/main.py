from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi import Request
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.logging_config import configure_logging


settings = get_settings()
logger = configure_logging(settings.log_level)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("ServiceOps application starting")
    try:
        yield
    finally:
        logger.info("ServiceOps application shutting down")


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.exception_handler(Exception)
async def handle_unexpected_error(request: Request, exc: Exception):
    logger.error(
        "Unhandled exception: %s %s",
        request.method,
        request.url.path,
        exc_info=(type(exc), exc, exc.__traceback__),
    )

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
