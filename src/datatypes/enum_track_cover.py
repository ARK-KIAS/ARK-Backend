import enum

class TrackCover(str, enum.Enum):
    sand = "sand"
    grass = "grass"
    other = "other"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum