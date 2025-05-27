from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.users_schema import UsersCreate, UsersUpdate, UsersResponse
from src.repositories.users_repository import users_repository

user_router = APIRouter(prefix="/admin", tags=["admin-users"])

@user_router.post('/user')
async def add_user(payload: UsersCreate):
    if await users_repository.get_single(email=payload.email) is not None:
        return JSONResponse(content={'message': 'This email already exists!'}, status_code=409)

    if await users_repository.get_single(username = payload.username) is not None:
        return JSONResponse(content={'message': 'This username already taken!'}, status_code=409)

    out = await users_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@user_router.get('/users', response_model=UsersResponse)
async def get_users():
    users = await users_repository.get_multi()

    return JSONResponse(content={'users': jsonable_encoder(users)}, status_code=200)

@user_router.get('/user/{id}', response_model=UsersResponse)
async def get_user_by_id(id: int):
    user = await users_repository.get_single(id=id)
    return JSONResponse(content={'user': jsonable_encoder(user)}, status_code=200)


@user_router.put('/user/{id}', response_model=UsersResponse)
async def update_user_by_id(payload:UsersUpdate):
    if await users_repository.get_single(email=payload.email) is not None:
        return JSONResponse(content={'message': 'This email already exists!'}, status_code=409)

    if await users_repository.get_single(username = payload.username) is not None:
        return JSONResponse(content={'message': 'This username already taken!'}, status_code=409)

    updated_user = await users_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_user)}, status_code=200)

@user_router.delete('/user/{id}')
async def delete_user_by_id(id: int):
    await users_repository.delete(id=id)
    return JSONResponse(content={'status': 'success'}, status_code=200)
