from enum import Enum


class GetUserResponse200SamlAccountsItemVerificationType3Type0Strategy(str, Enum):
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)