import enum

class UsageDirection(enum.Enum):
    riding = 1
    productive = 2
    decorative = 3
    duty = 4
    hard_duty = 5
    universal = 6
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum