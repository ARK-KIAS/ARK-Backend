from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.encoders import jsonable_encoder

from src.repositories.media_files_groups_repository import media_files_groups_repository
from src.repositories.media_files_repository import media_files_repository
from src.schemas.media_files_schema import MediaFilesResponse
from src.models.media_files_groups_model import MediaFilesGroupsModel
from src.models.media_files_model import MediaFilesModel

document_router = APIRouter(prefix="/document", tags=["document"])

@document_router.get('', response_model=MediaFilesResponse)
async def get_orgs():
    docs = await media_files_repository.get_multi()
    groups = await media_files_groups_repository.get_multi()

    docs_dict = []
    for doc in docs:
        for group in groups:
            if doc.group_id == group.id:
                dict = doc.__dict__
                dict["group_name"] = group.name
                docs_dict.append(dict)
                break

    return JSONResponse(content={'documents': jsonable_encoder(docs_dict)}, status_code=200)

@document_router.get('/{id}', response_model=MediaFilesResponse)
async def get_orgs(id: int):
    docs = await media_files_repository.get_single(id=id)

    if docs is None:
        return JSONResponse(content={'message': 'There is no file with that ID!'}, status_code=404)

    groups = await media_files_groups_repository.get_multi()

    docs_dict = {}
    for group in groups:
        if docs.group_id == group.id:
            docs_dict = docs.__dict__
            docs_dict["group_name"] = group.name
            break

    return JSONResponse(content={'horses': jsonable_encoder(docs_dict)}, status_code=200)