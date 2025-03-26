import enum

class TrackStatus(enum.Enum):
    dry = 1
    wet = 2
    other = 3
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum