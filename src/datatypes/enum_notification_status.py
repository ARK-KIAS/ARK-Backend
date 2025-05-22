import enum

class NotificationStatus(str, enum.Enum):
    success = 'success',
    danger = 'attention',
    error = 'critical',
    default = 'default',
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum