from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.lock_user_response_200_email_addresses_item_verification_type_0_status import (
    LockUserResponse200EmailAddressesItemVerificationType0Status,
)
from ..models.lock_user_response_200_email_addresses_item_verification_type_0_strategy import (
    LockUserResponse200EmailAddressesItemVerificationType0Strategy,
)

T = TypeVar("T", bound="LockUserResponse200EmailAddressesItemVerificationType0")


@_attrs_define
class LockUserResponse200EmailAddressesItemVerificationType0:
    """
    Attributes:
        status (LockUserResponse200EmailAddressesItemVerificationType0Status):
        strategy (LockUserResponse200EmailAddressesItemVerificationType0Strategy):
        attempts (int):
        expire_at (int):
    """

    status: LockUserResponse200EmailAddressesItemVerificationType0Status
    strategy: LockUserResponse200EmailAddressesItemVerificationType0Strategy
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
        status = LockUserResponse200EmailAddressesItemVerificationType0Status(d.pop("status"))

        strategy = LockUserResponse200EmailAddressesItemVerificationType0Strategy(d.pop("strategy"))

        attempts = d.pop("attempts")

        expire_at = d.pop("expire_at")

        lock_user_response_200_email_addresses_item_verification_type_0 = cls(
            status=status,
            strategy=strategy,
            attempts=attempts,
            expire_at=expire_at,
        )

        return lock_user_response_200_email_addresses_item_verification_type_0