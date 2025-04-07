import enum

class UsageDirection(str, enum.Enum):
    riding = "riding"
    productive = "productive"
    decorative = "decorative"
    duty = "duty"
    hard_duty = "hard_duty"
    universal = "universal"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum