import enum

class BonitationStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    canceled = "canceled"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum