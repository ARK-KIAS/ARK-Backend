import enum

class LifeStatus(enum.Enum):
    born = 1
    foal = 2
    active = 3
    grand = 4
    semen = 5
    dead = 6
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum