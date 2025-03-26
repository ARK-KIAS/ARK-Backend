import enum

class NotificationType(enum.Enum):
    general = "general"
    task = "task"
    none = "none"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum