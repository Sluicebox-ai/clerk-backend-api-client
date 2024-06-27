from enum import Enum


class GetUserListResponse200ItemEmailAddressesItemVerificationType2Strategy(str, Enum):
    OAUTH_CUSTOM_MOCK = "oauth_custom_mock"
    OAUTH_GOOGLE = "oauth_google"
    OAUTH_MOCK = "oauth_mock"

    def __str__(self) -> str:
        return str(self.value)
