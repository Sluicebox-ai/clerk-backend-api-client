from enum import Enum


class BanUserResponse200EmailAddressesItemVerificationType1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)