from enum import Enum


class GetUserResponse200EmailAddressesItemVerificationType1Strategy(str, Enum):
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
