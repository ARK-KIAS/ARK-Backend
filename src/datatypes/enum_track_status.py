import enum

class TrackStatus(str, enum.Enum):
    dry = "dry"
    wet = "wet"
    other = "other"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum