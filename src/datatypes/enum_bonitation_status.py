import enum

class BonitationStatus(enum.Enum):
    pending = 1
    approved = 2
    rejected = 3
    canceled = 4
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum