import enum

class SpecialistQualification(str, enum.Enum):
    trainer = "trainer"
    trainer_assistant = "trainer_assistant"
    jockey = "jockey"
    jockey_apprentice = "jockey_apprentice"
    trainee_traveler = "trainee_traveler"
    jockey_amateur = "jockey_amateur"
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum