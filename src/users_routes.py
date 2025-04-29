from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.users_schema import UsersCreate, UsersUpdate
from src.repositories.users_repository import users_repository

RANDOM_COOKIE_ID = "isaugdiuadushadoisahn"

user_routes = APIRouter(prefix="/admin", tags=["admin-users"])

@user_routes.post('/user')
async def add_user(payload: UsersCreate):
    await users_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@user_routes.get('/users')
async def get_users():
    perm = await users_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@user_routes.get('/user/{id}')
async def get_user_by_id(id: int):
    perm = await users_repository.get_single(id=id)

    return {'status': 'success', 'perm': perm}



@user_routes.put('/user/{id}')
async def update_user_by_id(payload:UsersUpdate):
    perm = await users_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@user_routes.delete('/user/{id}')
async def delete_user_by_id(payload:UsersUpdate):
    perm = await users_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

