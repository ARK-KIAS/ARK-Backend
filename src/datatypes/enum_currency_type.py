import enum

class CurrencyType(str, enum.Enum):
    rur = "rur"
    usd = "usd"
    eur = "eur"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum