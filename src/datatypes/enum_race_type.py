import enum

class RaceType(str, enum.Enum):
    race = "race"
    gallop = "gallop"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum