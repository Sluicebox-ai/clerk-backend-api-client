from enum import Enum


class UpdateUserResponse200PhoneNumbersItemVerificationType2Type0Status(str, Enum):
    EXPIRED = "expired"
    FAILED = "failed"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
