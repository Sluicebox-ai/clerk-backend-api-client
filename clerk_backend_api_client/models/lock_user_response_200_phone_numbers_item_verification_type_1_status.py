from enum import Enum


class LockUserResponse200PhoneNumbersItemVerificationType1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)