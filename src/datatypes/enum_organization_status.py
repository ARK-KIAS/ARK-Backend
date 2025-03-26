import enum

class OrganizationStatus(enum.Enum):
    not_activated = 1
    active = 2
    deleted = 3