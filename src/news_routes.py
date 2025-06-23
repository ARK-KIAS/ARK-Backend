from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.misc_functions import is_authorized
from src.repositories.media_files_repository import media_files_repository
from src.repositories.news_repository import news_repository
from src.schemas.news_schema import NewsResponse, NewsQuery, NewsCreate, NewsUpdate
from src.schemas.query_helper import MiscRequest

news_router = APIRouter(prefix="/news", tags=["news"])

@news_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: NewsCreate):
    out = await news_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@news_router.get('', response_model=NewsResponse)
async def get_orgs_by_filter(params: NewsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await news_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'news': jsonable_encoder(horses)}, status_code=200)

@news_router.get('/{id}', response_model=NewsResponse)
async def get_orgs(id: int):
    news = await news_repository.get_single(id=id)

    if news is None:
        return JSONResponse(content={'message': 'There is no bonitation with that ID!'}, status_code=404)

    return JSONResponse(content={'news': jsonable_encoder(news)}, status_code=200)


@news_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=NewsResponse)
async def update_org(id: int, payload:NewsUpdate):
    if await news_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no news with that ID!'}, status_code=404)

    news = await news_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(news)}, status_code=200)

@news_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    news = await news_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
