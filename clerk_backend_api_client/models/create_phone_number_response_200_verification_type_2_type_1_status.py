from enum import Enum


class CreatePhoneNumberResponse200VerificationType2Type1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)