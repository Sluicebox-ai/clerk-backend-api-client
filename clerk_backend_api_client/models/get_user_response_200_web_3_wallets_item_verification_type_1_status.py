from enum import Enum


class GetUserResponse200Web3WalletsItemVerificationType1Status(str, Enum):
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)