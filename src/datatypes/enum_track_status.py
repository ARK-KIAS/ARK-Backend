import enum

class TrackStatus(enum.Enum):
    dry = "dry"
    wet = "wet"
    other = "other"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum