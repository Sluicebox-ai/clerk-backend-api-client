from enum import Enum


class BanUserResponse200PhoneNumbersItemVerificationType2Type1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)