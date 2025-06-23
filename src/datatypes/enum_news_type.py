import enum

class NewsType(str, enum.Enum):
    common = "common"
    international = "international"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum