from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.media_files_repository import media_files_repository
from src.repositories.specialists_repository import specialists_repository
from src.schemas.query_helper import MiscRequest
from src.schemas.specialist_docs_schema import SpecialistDocsCreate, SpecialistDocsUpdate, SpecialistDocsResponse, \
    SpecialistDocsQuery
from src.repositories.specialist_docs_repository import specialist_docs_repository
from src.misc_functions import is_authorized

specialist_docs_router = APIRouter(prefix="/specialists_docs", tags=["specialists_docs"])

@specialist_docs_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: SpecialistDocsCreate):
    if await specialists_repository.get_single(id=payload.specialist_id) is None:
        return JSONResponse(content={'message': 'There is no specialist with that ID!'}, status_code=404)

    if await media_files_repository.get_single(id=payload.file_id) is None:
        return JSONResponse(content={'message': 'There is no file with that ID!'}, status_code=404)

    out = await specialist_docs_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@specialist_docs_router.get('', dependencies=[Depends(is_authorized)], response_model=SpecialistDocsResponse)
async def get_orgs_by_filter(params: SpecialistDocsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await specialist_docs_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'specialist_docs': jsonable_encoder(horses)}, status_code=200)

@specialist_docs_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=SpecialistDocsResponse)
async def get_orgs(id: int):
    specialist_docs = await specialist_docs_repository.get_single(id=id)

    if specialist_docs is None:
        return JSONResponse(content={'message': 'There is no specialist_docs with that ID!'}, status_code=404)

    return JSONResponse(content={'horse': jsonable_encoder(specialist_docs)}, status_code=200)


@specialist_docs_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=SpecialistDocsResponse)
async def update_org(id: int, payload:SpecialistDocsUpdate):
    if await specialist_docs_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no specialist-docs with that ID!'}, status_code=404)

    if await specialists_repository.get_single(id=payload.specialist_id) is None:
        return JSONResponse(content={'message': 'There is no specialist with that ID!'}, status_code=404)

    if await media_files_repository.get_single(id=payload.file_id) is None:
        return JSONResponse(content={'message': 'There is no file with that ID!'}, status_code=404)

    updated_specialist_docs = await specialist_docs_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_specialist_docs)}, status_code=200)

@specialist_docs_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    specialist_docs = await specialist_docs_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)