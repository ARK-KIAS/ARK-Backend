from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.repositories.organizations_repository import organizations_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

from .misc_functions import is_authorized


organization_router = APIRouter(prefix="/organization", tags=["organizations"])

# Organization Repos ###################################################################################################
@organization_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: OrganizationsCreate):
    await organizations_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@organization_router.get('/', dependencies=[Depends(is_authorized)])
async def get_orgs():
    orgs = await organizations_repository.get_multi()

    return JSONResponse(content={'organizations': jsonable_encoder(orgs)}, status_code=200)

@organization_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    org = await organizations_repository.get_single(id=id)

    return JSONResponse(content={'organization': jsonable_encoder(org)}, status_code=200)


@organization_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:OrganizationsUpdate):
    updated_org = await organizations_repository.update(payload, id=payload.id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_org)}, status_code=200)

@organization_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    org = await organizations_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})

