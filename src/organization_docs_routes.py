from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.organizations_docs_schema import OrganizationsDocsCreate, OrganizationsDocsUpdate, OrganizationsDocsResponse
from src.repositories.organizations_docs_repository import organizations_docs_repository

from .misc_functions import is_authorized

organization_docs_router = APIRouter(prefix="/organization/docs", tags=["organization_docs"])

@organization_docs_router.get('/')
async def add_permission():
    return JSONResponse(content={'status': 'success'}, status_code=200)

@organization_docs_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: OrganizationsDocsCreate):
    await organizations_docs_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@organization_docs_router.get('/', dependencies=[Depends(is_authorized)], response_model=OrganizationsDocsCreate)
async def get_orgs():
    organizations_docs = await organizations_docs_repository.get_multi()

    return JSONResponse(content={'organizations_docs': jsonable_encoder(organizations_docs)}, status_code=200)
    #return organizations_docs

@organization_docs_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    organizations_docs = await organizations_docs_repository.get_single(id=id)

    return JSONResponse(content={'race_days': jsonable_encoder(organizations_docs)}, status_code=200)


@organization_docs_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:OrganizationsDocsUpdate):
    updated_organizations_docs = await organizations_docs_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_organizations_docs)}, status_code=200)

@organization_docs_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    organizations_docs = await organizations_docs_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
