from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.users_schema import UsersCreate, UsersUpdate, UsersResponse
from src.repositories.users_repository import users_repository

race_routes = APIRouter(prefix="/races", tags=["races"])

@race_routes.get('/')
async def add_permission():
    return JSONResponse(content={'status': 'success'}, status_code=200)
