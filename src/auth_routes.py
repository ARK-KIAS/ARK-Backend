import uuid

from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.permissions_repository import permissions_repository
from src.schemas.redis_sessions_schema import RedisSessionsCreate, RedisSessionsUpdate, RedisSessionsAuth, RedisSessionsBase
from src.schemas.users_schema import UsersResponse

from src.repositories.organizations_repository import organizations_repository
from src.repositories.users_repository import users_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

from .misc_functions import is_authorized

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post('/login/user')
async def check_auth(payload: RedisSessionsAuth):
    password = payload.password
    username = payload.username

    auth_user = await users_repository.get_single(username=username, password=password)

    if auth_user is None:
        return JSONResponse(content={"message": "Auth failure, check login/password"}, status_code=401)

    response = JSONResponse(content={'status': 'success'})
    users_sessions = uuid.uuid4()

    response.set_cookie(key="session_cookie", value=str(users_sessions), max_age=604800, httponly=True)

    payload_dict = payload.dict()
    payload_dict["user_id"] = auth_user.id
    payload_dict["access_token"] = users_sessions
    create_model = RedisSessionsCreate(**payload_dict)

    await redis_sessions_repository.create(create_model)

    return response

@auth_router.get('/login/user', dependencies=[Depends(is_authorized)])
async def is_logged(req: Request):
    session_id = req.cookies.get("session_cookie")
    login = await redis_sessions_repository.get_single(access_token=session_id)

    user = await users_repository.get_single(id=login.user_id)
    user_dict = user.__dict__
    user_dict.pop("password")

    org = await organizations_repository.get_single(id=user.organization_id)

    perm = await permissions_repository.get_single(id=user.permission_id)

    return JSONResponse(content={'user': jsonable_encoder(user_dict), 'org': jsonable_encoder(org), 'permission': jsonable_encoder(perm)}, status_code=200)

@auth_router.delete('/logout/user')
async def logout(req: Request):
    session_id = req.cookies.get("session_cookie")
    resp = JSONResponse(content={'status': 'success'}) #todo
    perm = await redis_sessions_repository.delete(access_token=session_id)
    resp.delete_cookie(key="session_cookie")
    return resp