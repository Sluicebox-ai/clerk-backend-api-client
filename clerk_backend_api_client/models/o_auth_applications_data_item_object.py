from enum import Enum


class OAuthApplicationsDataItemObject(str, Enum):
    OAUTH_APPLICATION = "oauth_application"

    def __str__(self) -> str:
        return str(self.value)
