from copy import deepcopy
from typing import Any, Tuple, Optional, TypeVar, Type

from pydantic import BaseModel, create_model, Field
from pydantic.fields import FieldInfo

########################################################################################################################
def make_field_optional(field: FieldInfo, default: Any = None) -> Tuple[Any, FieldInfo]:
  new = deepcopy(field)
  new.default = default
  new.annotation = Optional[field.annotation]  # type: ignore
  return (new.annotation, new)


BaseModelT = TypeVar('BaseModelT', bound=BaseModel)


def make_partial_model(model: Type[BaseModelT]) -> Type[BaseModelT]:
  return create_model(  # type: ignore
    f'Partial{model.__name__}',
    __base__=model,
    __module__=model.__module__,
    **{
        field_name: make_field_optional(field_info)
        for field_name, field_info in model.model_fields.items()
    }
    )
########################################################################################################################

class MiscRequest(BaseModel):
    order: Optional[str] = Field("id")
    limit: Optional[int] = Field(100)
    offset: Optional[int] = Field(0)
