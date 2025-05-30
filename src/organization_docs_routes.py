from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.organizations_docs_schema import OrganizationsDocsCreate, OrganizationsDocsUpdate, \
    OrganizationsDocsResponse, OrganizationsDocsQuery
from src.repositories.organizations_docs_repository import organizations_docs_repository
from src.repositories.organizations_repository import organizations_repository

from .misc_functions import is_authorized
from .repositories.media_files_repository import media_files_repository
from .schemas.query_helper import MiscRequest

organization_docs_router = APIRouter(prefix="/organization_docs", tags=["organization_docs"])

@organization_docs_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: OrganizationsDocsCreate):
    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    if await media_files_repository.get_single(id=payload.file_id) is None:
        return JSONResponse(content={'message': 'There is no file with that ID!'}, status_code=404)

    out = await organizations_docs_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@organization_docs_router.get('', dependencies=[Depends(is_authorized)], response_model=OrganizationsDocsResponse)
async def get_orgs_by_filter(params: OrganizationsDocsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await organizations_docs_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'organizations_docs': jsonable_encoder(horses)}, status_code=200)

@organization_docs_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=OrganizationsDocsResponse)
async def get_orgs(id: int):
    organizations_docs = await organizations_docs_repository.get_single(id=id)

    if organizations_docs is None:
        return JSONResponse(content={'message': 'There is no organizations_docs with that ID!'}, status_code=404)

    return JSONResponse(content={'race_days': jsonable_encoder(organizations_docs)}, status_code=200)


@organization_docs_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=OrganizationsDocsResponse)
async def update_org(id: int, payload:OrganizationsDocsUpdate):
    if await organizations_docs_repository.get_single(id=payload.id) is None:
        return JSONResponse(content={'message': 'There is no organization-docs with that ID!'}, status_code=404)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    if await media_files_repository.get_single(id=payload.file_id) is None:
        return JSONResponse(content={'message': 'There is no file with that ID!'}, status_code=404)

    updated_organizations_docs = await organizations_docs_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_organizations_docs)}, status_code=200)

@organization_docs_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    organizations_docs = await organizations_docs_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
