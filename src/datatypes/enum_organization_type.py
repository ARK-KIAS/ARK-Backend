import enum

class OrganizationType(enum.Enum):
    hippodrome = 1
    breeder = 2
    reproducer = 3
    entity = 4
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum