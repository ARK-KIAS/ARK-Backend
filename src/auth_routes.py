import uuid

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.schemas.redis_sessions_schema import RedisSessionsCreate, RedisSessionsUpdate, RedisSessionsAuth, RedisSessionsBase

from src.repositories.users_repository import users_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post('/login/user')
async def check_auth(payload: RedisSessionsAuth):
    password = payload.password
    username = payload.username

    auth_user = await users_repository.get_single(username=username, password=password)

    if auth_user is None:
        return JSONResponse(content={"message": "Auth failure, check login/password"}, status_code=401)

    response = RedirectResponse("/", status_code=200) #todo
    users_sessions = uuid.uuid4()

    response.set_cookie(key="session_cookie", value=str(users_sessions))

    payload_dict = payload.dict()
    payload_dict["user_id"] = auth_user.id
    payload_dict["access_token"] = users_sessions
    create_model = RedisSessionsCreate(**payload_dict)

    await redis_sessions_repository.create(create_model)

    return response

@auth_router.delete('/logout/user')
async def logout(req: Request):
    session_id = req.cookies.get("session_cookie")
    resp = RedirectResponse("/", status_code=200) #todo
    perm = await redis_sessions_repository.delete(access_token=session_id)
    resp.delete_cookie(key="session_cookie")
    return resp