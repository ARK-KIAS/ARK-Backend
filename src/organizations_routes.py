from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate, OrganizationsResponse
from src.repositories.organizations_repository import organizations_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

from .misc_functions import is_authorized


organization_router = APIRouter(prefix="/organizations", tags=["organizations"])

# Organization Repos ###################################################################################################
@organization_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: OrganizationsCreate):
    if await organizations_repository.get_single(corr_account=payload.corr_account):
        return JSONResponse(content={'message': 'Organization with this corr account already exists!'}, status_code=409)

    if await organizations_repository.get_single(email=payload.email):
        return JSONResponse(content={'message': 'Organization with this email already exists!'}, status_code=409)

    if await organizations_repository.get_single(settlement_account=payload.settlement_account):
        return JSONResponse(content={'message': 'Organization with this settlement account already exists!'}, status_code=409)

    if await organizations_repository.get_single(site_link=payload.site_link):
        return JSONResponse(content={'message': 'Organization with this site link already exists!'}, status_code=409)

    if await organizations_repository.get_single(tel=payload.tel):
        return JSONResponse(content={'message': 'Organization with this telephone number already exists!'}, status_code=409)


    out = await organizations_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@organization_router.get('', dependencies=[Depends(is_authorized)], response_model=OrganizationsResponse)
async def get_orgs():
    orgs = await organizations_repository.get_multi()

    return JSONResponse(content={'organizations': jsonable_encoder(orgs)}, status_code=200)

@organization_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=OrganizationsResponse)
async def get_orgs(id: int):
    org = await organizations_repository.get_single(id=id)

    if org is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    return JSONResponse(content={'organizations': jsonable_encoder(org)}, status_code=200)


@organization_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=OrganizationsResponse)
async def update_org(id: int, payload:OrganizationsUpdate):
    if await organizations_repository.get_single(corr_account=payload.corr_account):
        return JSONResponse(content={'message': 'Organization with this corr account already exists!'}, status_code=409)

    if await organizations_repository.get_single(email=payload.email):
        return JSONResponse(content={'message': 'Organization with this email already exists!'}, status_code=409)

    if await organizations_repository.get_single(settlement_account=payload.settlement_account):
        return JSONResponse(content={'message': 'Organization with this settlement account already exists!'}, status_code=409)

    if await organizations_repository.get_single(site_link=payload.site_link):
        return JSONResponse(content={'message': 'Organization with this site link already exists!'}, status_code=409)

    if await organizations_repository.get_single(tel=payload.tel):
        return JSONResponse(content={'message': 'Organization with this telephone number already exists!'}, status_code=409)

    updated_org = await organizations_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_org)}, status_code=200)

@organization_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    org = await organizations_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})

