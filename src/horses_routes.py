from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.redis_sessions_repository import redis_sessions_repository
from src.repositories.horses_repository import horses_repository
from src.schemas.horses_schema import HorsesCreate, HorsesUpdate, HorsesResponse
from src.schemas.horse_history_schema import HorseHistoryCreate

from .misc_functions import is_authorized, is_inspector
from .repositories.bonitation_horses_repository import bonitation_horses_repository
from .repositories.bonitations_repository import bonitations_repository
from .repositories.breeds_repository import breeds_repository
from .repositories.horse_history_repository import horse_history_repository
from .repositories.organizations_repository import organizations_repository
from .repositories.regions_repository import regions_repository
from .schemas.bonitation_horses_schema import BonitationHorsesUpdate
from .schemas.bonitations_schema import BonitationsUpdate

horses_router = APIRouter(prefix="/horses", tags=["horses"])

@horses_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorsesCreate):
    if await regions_repository.get_single(id=payload.birth_region_id) is None:
        return JSONResponse(content={'message': 'There is no region with that ID!'}, status_code=404)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    if await breeds_repository.get_single(id=payload.breed_id) is None:
        return JSONResponse(content={'message': 'There is no breed with that ID!'}, status_code=404)

    out = await horses_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@horses_router.get('', response_model=HorsesResponse)
async def get_orgs():
    horses = await horses_repository.get_multi()

    return JSONResponse(content={'horses': jsonable_encoder(horses)}, status_code=200)
    #return horses

@horses_router.get('/{id}', response_model=HorsesResponse)
async def get_orgs(id: int):
    horses = await horses_repository.get_single(id=id)

    if horses is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    return JSONResponse(content={'horses': jsonable_encoder(horses)}, status_code=200)

@horses_router.get('', response_model=HorsesResponse)
async def get_orgs_by_filter(params: HorsesResponse = Depends()):
    horses = await horses_repository.get_multi_filtered(filter=params.model_fields)

    return JSONResponse(content={'horses': jsonable_encoder(horses)}, status_code=200)


@horses_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesResponse)
async def update_org(id: int, payload:HorsesUpdate):
    if await horses_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    if await regions_repository.get_single(id=payload.birth_region_id) is None:
        return JSONResponse(content={'message': 'There is no region with that ID!'}, status_code=404)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    if await breeds_repository.get_single(id=payload.breed_id) is None:
        return JSONResponse(content={'message': 'There is no breed with that ID!'}, status_code=404)

    updated_horse = await horses_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse)}, status_code=200)

@horses_router.patch('/{id}', dependencies=[Depends(is_inspector)], response_model=HorsesResponse)
async def update_org(id: int, payload:HorseHistoryCreate):
    #Переводим пэйлоад в словарь и убираем horse_id
    payload_dict = payload.dict()
    payload_dict["id"] = payload.horse_id
    payload_dict.pop("horse_id")
    horse_model = HorsesUpdate(**payload_dict)

    #Проверяем что такая лошадь есть
    if horses_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    #Обновляем данные бонитировки
    updated_horse = await horses_repository.update(horse_model, id=id)

    #Добавляем данные бонитировки в историю лошадей
    await horse_history_repository.create(payload)

    #Достаем объект bonitation_horses для текущей лошади, если текущая лошадь уже появлялась в этой бонитировке, херачим 404
    bonitation_horses = await bonitation_horses_repository.get_single(horse_id=id, is_ready=False)

    if bonitation_horses is None:
        return JSONResponse(content={'message': 'There is no bonitation_horse pair with that horse ID!'}, status_code=404)

    #Переводим объект лошади-бонитировки в словарь и говорим что лошадь прошла бонитировку
    bonitation_horses_dict = bonitation_horses.__dict__
    bonitation_horses_dict["is_ready"] = True
    bonitation_horses_model = BonitationHorsesUpdate(**bonitation_horses_dict)

    #Обнавляем в базе связь лошади-бонитировки
    await bonitation_horses_repository.update(bonitation_horses_model, id=bonitation_horses_model.id)

    #Достаём всех лоашдей, из текущей бонитировки, что не прошли бонитировку - is_ready=False
    bonitation_full_horses = await bonitation_horses_repository.get_multi_filtered(bonitation_id=bonitation_horses.bonitation_id, is_ready=False)

    #Если такие лошади нашлись, едем дальше, если нет, то объявлем бонитировку законченой - ["is_finished"] = True
    if len(bonitation_full_horses) > 0:
        return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse)}, status_code=200)
    else:
        bonitation = await bonitations_repository.get_single(id=bonitation_horses.bonitation_id)
        bonitation_dict = bonitation.__dict__
        bonitation_dict["is_finished"] = True
        bonitation_model = BonitationsUpdate(**bonitation_dict)

        await bonitations_repository.update(bonitation_model, id=bonitation_model.id)

        return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse)}, status_code=200)


@horses_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horse = await horses_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})