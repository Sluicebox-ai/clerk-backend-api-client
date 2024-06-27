from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.get_user_list_response_200_item_email_addresses_item_verification_type_0_status import (
    GetUserListResponse200ItemEmailAddressesItemVerificationType0Status,
)
from ..models.get_user_list_response_200_item_email_addresses_item_verification_type_0_strategy import (
    GetUserListResponse200ItemEmailAddressesItemVerificationType0Strategy,
)

T = TypeVar("T", bound="GetUserListResponse200ItemEmailAddressesItemVerificationType0")


@_attrs_define
class GetUserListResponse200ItemEmailAddressesItemVerificationType0:
    """
    Attributes:
        status (GetUserListResponse200ItemEmailAddressesItemVerificationType0Status):
        strategy (GetUserListResponse200ItemEmailAddressesItemVerificationType0Strategy):
        attempts (int):
        expire_at (int):
    """

    status: GetUserListResponse200ItemEmailAddressesItemVerificationType0Status
    strategy: GetUserListResponse200ItemEmailAddressesItemVerificationType0Strategy
    attempts: int
    expire_at: int

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        strategy = self.strategy.value

        attempts = self.attempts

        expire_at = self.expire_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "strategy": strategy,
                "attempts": attempts,
                "expire_at": expire_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = GetUserListResponse200ItemEmailAddressesItemVerificationType0Status(d.pop("status"))

        strategy = GetUserListResponse200ItemEmailAddressesItemVerificationType0Strategy(d.pop("strategy"))

        attempts = d.pop("attempts")

        expire_at = d.pop("expire_at")

        get_user_list_response_200_item_email_addresses_item_verification_type_0 = cls(
            status=status,
            strategy=strategy,
            attempts=attempts,
            expire_at=expire_at,
        )

        return get_user_list_response_200_item_email_addresses_item_verification_type_0
