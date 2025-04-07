import enum

class RaceCategoryType(str, enum.Enum):
    commerce = "commerce"
    traditional = "traditional"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum