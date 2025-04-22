import uvicorn
from fastapi import FastAPI
from src.config.project_config import settings
from src.routes import perm_router


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION
    )
    application.include_router(perm_router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
