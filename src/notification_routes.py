from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.notifications_repository import notifications_repository
from src.repositories.users_repository import users_repository
from src.schemas.notifications_schema import NotificationsCreate
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.repositories.organizations_repository import organizations_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

from .misc_functions import is_authorized

notification_router = APIRouter(prefix="/notification", tags=["notifications"])

async def get_authorized_user_id(id):
    auth = await users_repository.get_single(id=id)
    return auth


# Organization Repos ###################################################################################################
@notification_router.post('/', dependencies=[Depends(is_authorized)])
async def create_notification(payload: NotificationsCreate):
    await notifications_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@notification_router.get('/', dependencies=[Depends(is_authorized)])
async def get_all_notifications():
    notification = await notifications_repository.get_multi()

    return JSONResponse(content={'notification': jsonable_encoder(notification)}, status_code=200)

@notification_router.get('/{org_id}', dependencies=[Depends(is_authorized)])
async def get_notifications_for_orgs(org_id: int, req: Request):
    session_id = req.cookies.get("session_cookie")
    auth = await redis_sessions_repository.get_single(access_token=session_id)

    org = await organizations_repository.get_single(admin_id=auth.user_id)
    nots = await notifications_repository.get_multi_filtered(user_id=auth.user_id) #todo 3 бонитировщика а уведы только админу

    return JSONResponse(content={'notifications': jsonable_encoder(nots)}, status_code=200)
