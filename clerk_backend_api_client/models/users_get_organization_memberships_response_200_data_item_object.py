from enum import Enum


class UsersGetOrganizationMembershipsResponse200DataItemObject(str, Enum):
    ORGANIZATION_MEMBERSHIP = "organization_membership"

    def __str__(self) -> str:
        return str(self.value)
