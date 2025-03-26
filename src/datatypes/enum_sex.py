import enum

class Sex(enum.Enum):
    male = "male"
    female = "female"
    none = "none"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum