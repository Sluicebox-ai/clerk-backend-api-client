from enum import Enum


class UnbanUserResponse200PasskeysItemVerificationType2Type0Strategy(str, Enum):
    PASSKEY = "passkey"

    def __str__(self) -> str:
        return str(self.value)