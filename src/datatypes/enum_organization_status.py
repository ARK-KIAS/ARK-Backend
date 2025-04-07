import enum

class OrganizationStatus(str, enum.Enum):
    not_activated = "not_activated"
    active = "active"
    deleted = "deleted"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum