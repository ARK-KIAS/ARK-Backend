import enum

class SpecialistQualification(enum.Enum):
    trainer = 1
    trainer_assistant = 2
    jockey = 3
    jockey_apprentice = 4
    trainee_traveler = 5
    jockey_amateur = 6
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum