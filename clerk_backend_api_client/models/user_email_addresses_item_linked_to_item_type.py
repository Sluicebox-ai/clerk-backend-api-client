from enum import Enum


class UserEmailAddressesItemLinkedToItemType(str, Enum):
    OAUTH_GOOGLE = "oauth_google"
    OAUTH_MOCK = "oauth_mock"
    SAML = "saml"

    def __str__(self) -> str:
        return str(self.value)