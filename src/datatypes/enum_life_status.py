import enum

class LifeStatus(str, enum.Enum):
    born = "born"
    foal = "foal"
    active = "active"
    grand = "grand"
    semen = "semen"
    dead = "dead"
    none = "none"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum