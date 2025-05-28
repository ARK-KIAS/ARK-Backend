from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.media_files_repository import media_files_repository
from src.schemas.media_files_schema import MediaFilesCreate, MediaFilesResponse, MediaFilesUpdate

from .misc_functions import is_authorized

media_router = APIRouter(prefix="/media", tags=["media"])

@media_router.post('', dependencies=[Depends(is_authorized)])
async def add_media_file(payload: MediaFilesCreate):

    return JSONResponse(content={'status': 'success'}, status_code=201)

@media_router.get('', dependencies=[Depends(is_authorized)], response_model=MediaFilesResponse)
async def get_orgs():
    breeds = []
    return JSONResponse(content={'breeds': jsonable_encoder(breeds)}, status_code=200)

@media_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=MediaFilesResponse)
async def get_orgs(id: int):
    breed = {}
    return JSONResponse(content={'breed': jsonable_encoder(breed)}, status_code=200)


@media_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=MediaFilesResponse)
async def update_org(id: int, payload:MediaFilesUpdate):
    breeds = []
    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(breeds)}, status_code=200)

@media_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    breeds = []
    return JSONResponse(content={'status': 'success'})
