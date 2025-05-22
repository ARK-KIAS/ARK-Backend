import enum

class NotificationType(str, enum.Enum):
    bonitation = 'bonitation',
    message = 'message',
    check = 'check',
    request = 'request',