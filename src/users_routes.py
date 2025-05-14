from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.users_schema import UsersCreate, UsersUpdate, UsersResponse
from src.repositories.users_repository import users_repository

user_routes = APIRouter(prefix="/admin", tags=["admin-users"])

@user_routes.post('/user')
async def add_user(payload: UsersCreate):
    await users_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@user_routes.get('/users')
async def get_users():
    users = await users_repository.get_multi()

    return JSONResponse(content={'users': jsonable_encoder(users)}, status_code=200)

@user_routes.get('/user/{id}')
async def get_user_by_id(id: int):
    user = await users_repository.get_single(id=id)
    return JSONResponse(content={'user': jsonable_encoder(user)}, status_code=200)


@user_routes.put('/user/{id}')
async def update_user_by_id(payload:UsersUpdate):
    updated_user = await users_repository.update(payload, id=payload.id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_user)}, status_code=200)

@user_routes.delete('/user/{id}')
async def delete_user_by_id(id: int):
    await users_repository.delete(id=id)
    return JSONResponse(content={'status': 'success'}, status_code=200)
