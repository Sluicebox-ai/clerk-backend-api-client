from enum import Enum


class UnbanUserResponse200PhoneNumbersItemVerificationType3Type1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
