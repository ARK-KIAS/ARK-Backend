import enum

class OrganizationType(str, enum.Enum):
    hippodrome = "hippodrome"
    breeder = "breeder"
    reproducer = "reproducer"
    entity = "entity"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum