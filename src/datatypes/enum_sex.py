import enum

class Sex(enum.Enum):
    male = 1
    female = 2
    none = 3
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum