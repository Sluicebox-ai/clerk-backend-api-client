from enum import Enum


class UserPhoneNumbersItemVerificationType2Type1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
