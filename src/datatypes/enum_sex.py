import enum

class Sex(str, enum.Enum):
    male = "male"
    female = "female"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum