from enum import Enum


class UnbanUserResponse200EmailAddressesItemObject(str, Enum):
    EMAIL_ADDRESS = "email_address"

    def __str__(self) -> str:
        return str(self.value)
