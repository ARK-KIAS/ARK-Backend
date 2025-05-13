from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.repositories.organizations_repository import organizations_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

async def is_authorized(request: Request):
    """verify that user has a valid session"""
    session_id = request.cookies.get("session_cookie")
    if not session_id:
        raise HTTPException(status_code=401)

    auth = await redis_sessions_repository.get_single(access_token=session_id)

    if auth is None:
        raise HTTPException(status_code=403)
    return True