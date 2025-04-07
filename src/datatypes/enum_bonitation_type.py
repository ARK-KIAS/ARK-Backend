import enum

class BonitationType(str, enum.Enum):
    bonitation = "bonitation"
    chipization = "chipization"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum