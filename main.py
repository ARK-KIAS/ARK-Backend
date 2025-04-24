import uvicorn
from fastapi import FastAPI
from src.config.project_config import settings
from src.routes import main_router
from src.auth_routes import auth_router


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION
    )
    application.include_router(main_router)
    application.include_router(auth_router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
