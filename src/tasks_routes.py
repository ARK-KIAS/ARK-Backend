from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.misc_functions import is_authorized, is_inspector, get_authorized_user
from src.repositories.bonitation_horses_repository import bonitation_horses_repository
from src.repositories.horses_repository import horses_repository
from src.repositories.organizations_repository import organizations_repository
from src.repositories.users_repository import users_repository

from src.schemas.bonitations_schema import BonitationsCreate, BonitationsResponse, BonitationsUpdate
from src.repositories.bonitations_repository import bonitations_repository

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

@tasks_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: BonitationsCreate):
    if await users_repository.get_single(id=payload.inspector_id) is None:
        return JSONResponse(content={'message': 'There is no user with that ID!'}, status_code=404)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    await bonitations_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@tasks_router.get('', dependencies=[Depends(is_inspector)], response_model=BonitationsResponse)
async def get_orgs(req: Request):
    user = await get_authorized_user(req)
    bonitations = await bonitations_repository.get_multi_filtered(inspector_id=user.id)

    return JSONResponse(content={'tasks': jsonable_encoder(bonitations)}, status_code=200)
    #return bonitation

@tasks_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=BonitationsResponse)
async def get_orgs(id: int):
    bonitation = await bonitations_repository.get_single(id=id)

    if bonitation is None:
        return JSONResponse(content={'message': 'There is no task with that ID!'}, status_code=404)

    bonitation_horses = await bonitation_horses_repository.get_multi_filtered(bonitation_id=bonitation.id)

    if bonitation_horses is None:
        return JSONResponse(content={'message': 'There is no horses in task with that ID!'}, status_code=404)

    horses = []
    for bh in bonitation_horses:
        horse_dict = (await horses_repository.get_single(id=bh.horse_id)).__dict__
        horse_dict["is_ready"] = bh.is_ready
        horses.append(horse_dict)

    bonitation_dict = bonitation.__dict__

    bonitation_dict["horses"] = horses

    return JSONResponse(content={'task': jsonable_encoder(bonitation_dict)}, status_code=200)


@tasks_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=BonitationsResponse)
async def update_org(id: int, payload:BonitationsUpdate):
    if await bonitations_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no task with that ID!'}, status_code=404)

    if await users_repository.get_single(id=payload.inspector_id) is None:
        return JSONResponse(content={'message': 'There is no user with that ID!'}, status_code=404)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    bonitation = await bonitations_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(bonitation)}, status_code=200)

@tasks_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    bonitation = await bonitations_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)