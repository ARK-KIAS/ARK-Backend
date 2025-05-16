from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.specialist_docs_schema import SpecialistDocsCreate, SpecialistDocsUpdate, SpecialistDocsResponse
from src.repositories.specialist_docs_repository import specialist_docs_repository
from src.misc_functions import is_authorized

specialist_docs_router = APIRouter(prefix="/specialists/docs", tags=["specialists_docs"])

@specialist_docs_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: SpecialistDocsCreate):
    await specialist_docs_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@specialist_docs_router.get('/', dependencies=[Depends(is_authorized)], response_model=SpecialistDocsCreate)
async def get_orgs() -> list[SpecialistDocsResponse]:
    specialist_docs = await specialist_docs_repository.get_multi()

    # return JSONResponse(content={'specialist_docs': jsonable_encoder(specialist_docs)}, status_code=200)
    return specialist_docs

@specialist_docs_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    specialist_docs = await specialist_docs_repository.get_single(id=id)

    return JSONResponse(content={'horse': jsonable_encoder(specialist_docs)}, status_code=200)


@specialist_docs_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:SpecialistDocsUpdate):
    updated_specialist_docs = await specialist_docs_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_specialist_docs)}, status_code=200)

@specialist_docs_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    specialist_docs = await specialist_docs_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)