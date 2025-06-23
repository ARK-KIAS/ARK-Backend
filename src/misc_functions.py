from fastapi import HTTPException, Request

from src.repositories.permissions_repository import permissions_repository
from src.repositories.users_repository import users_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

inspector_permission_name = "inspector" #Important shit! Using this to differentiate between user and inspector!

async def is_authorized(request: Request):
    """verify that user has a valid session"""
    session_id = request.cookies.get("session_cookie")
    if not session_id:
        raise HTTPException(detail= "Not authorized!", status_code=401)

    auth = await redis_sessions_repository.get_single(access_token=session_id)

    if auth is None:
        raise HTTPException(detail= "Not authorized!", status_code=401)
    return True

########################################################################################################################
async def accessible(request: Request):
    session_id = request.cookies.get("session_cookie")
    if not session_id:
        raise HTTPException(detail= "Not authorized!", status_code=401)

    auth = await redis_sessions_repository.get_single(access_token=session_id)

    if auth is None:
        raise HTTPException(detail= "Not authorized!", status_code=401)

    user = await users_repository.get_single(id=auth.user_id)

    if user is None:
        raise HTTPException(detail= "User not found!", status_code=404)

    user_permission = await permissions_repository.get_single(id=user.permission_id)

    if user_permission is None:
        raise HTTPException(status_code=400)


    perm_list = ["accounts_all"," races_full", "bonitation_full",
                 "specialist_full" ,"files_full", "hold_horses",
                 "create_bonitations", "create_races"]

    request.base_url.path.find("")

    return True

########################################################################################################################
async def get_authorized_user(request: Request):
    session_id = request.cookies.get("session_cookie")

    if not session_id:
        raise HTTPException(detail="Not authorized!", status_code=401)

    auth = await redis_sessions_repository.get_single(access_token=session_id)

    if auth is None:
        raise HTTPException(detail="Not authorized!", status_code=401)

    user = await users_repository.get_single(id=auth.user_id)

    if user is None:
        raise HTTPException(detail="User not found!", status_code=404)

    return user

########################################################################################################################
async def is_inspector(request: Request):
    session_id = request.cookies.get("session_cookie")
    if not session_id:
        raise HTTPException(detail= "Not authorized!", status_code=401)

    auth = await redis_sessions_repository.get_single(access_token=session_id)

    if auth is None:
        raise HTTPException(detail= "Not authorized!", status_code=401)

    user = await users_repository.get_single(id=auth.user_id)

    if user is None:
        raise HTTPException(detail= "User not found!", status_code=404)

    user_permission = await permissions_repository.get_single(id=user.permission_id)

    if user_permission is None:
        raise HTTPException(detail="Somehow user without permission!", status_code=404)

    if user_permission.bonitation_full:
        return True
    else:
        raise HTTPException(detail="You are not inspector!", status_code=403)