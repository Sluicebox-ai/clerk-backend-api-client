from enum import Enum


class CreateUserResponse200EmailAddressesItemVerificationType1Strategy(str, Enum):
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
