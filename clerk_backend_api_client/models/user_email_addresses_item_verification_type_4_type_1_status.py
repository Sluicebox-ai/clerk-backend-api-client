from enum import Enum


class UserEmailAddressesItemVerificationType4Type1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)