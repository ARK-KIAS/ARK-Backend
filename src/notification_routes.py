from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse, Response
from sqlalchemy import desc

from src.repositories.notifications_repository import notifications_repository
from src.repositories.users_repository import users_repository
from src.schemas.notifications_schema import NotificationsCreate, NotificationsResponse, notifications_query_model
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.repositories.organizations_repository import organizations_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

from .misc_functions import is_authorized, get_authorized_user, is_inspector
from .models.notifications_model import NotificationsModel

notification_router = APIRouter(prefix="/notifications", tags=["notifications"])

# Organization Repos ###################################################################################################
@notification_router.post('', dependencies=[Depends(is_authorized)]) #todo доделать проверки входных данных
async def create_notification(payload: NotificationsCreate):
    out = await notifications_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@notification_router.get('', dependencies=[Depends(is_authorized)], response_model=NotificationsResponse)
async def get_all_notifications_for_user(req: Request):

    user = await get_authorized_user(req)

    notifications = await notifications_repository.get_multi_filtered(desc(NotificationsModel.created_at), 100, 0, user_id=user.id)

    return JSONResponse(content={'notifications': jsonable_encoder(notifications)}, status_code=200)

@notification_router.get('/user', dependencies=[Depends(is_authorized)], response_model=NotificationsResponse)
async def get_notifications_for_users(params: notifications_query_model = Depends()):
    params_dict = params.dict()
    nots = await notifications_repository.get_multi_filtered(user_id=params_dict["user_id"]) #todo 3 бонитировщика а уведы только админу

    return JSONResponse(content={'notifications': jsonable_encoder(nots)}, status_code=200)
