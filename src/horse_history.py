
from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.users_schema import UsersCreate, UsersUpdate, UsersResponse
from src.repositories.users_repository import users_repository

history_routes = APIRouter(prefix="/history", tags=["history"])

@history_routes.get('/')
async def add_permission():
    return JSONResponse(content={'status': 'success'}, status_code=200)
