from enum import Enum


class UnlockUserResponse200SamlAccountsItemVerificationType2Type0Strategy(str, Enum):
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)