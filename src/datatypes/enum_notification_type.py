import enum

class NotificationType(enum.Enum):
    general = 1
    task = 2
    none = 3
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum