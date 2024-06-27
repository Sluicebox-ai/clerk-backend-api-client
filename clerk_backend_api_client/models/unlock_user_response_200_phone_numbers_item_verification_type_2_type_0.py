from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.unlock_user_response_200_phone_numbers_item_verification_type_2_type_0_status import (
    UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Status,
)
from ..models.unlock_user_response_200_phone_numbers_item_verification_type_2_type_0_strategy import (
    UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Strategy,
)

T = TypeVar("T", bound="UnlockUserResponse200PhoneNumbersItemVerificationType2Type0")


@_attrs_define
class UnlockUserResponse200PhoneNumbersItemVerificationType2Type0:
    """
    Attributes:
        status (UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Status):
        strategy (UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Strategy):
        attempts (int):
        expire_at (int):
    """

    status: UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Status
    strategy: UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Strategy
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
        status = UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Status(d.pop("status"))

        strategy = UnlockUserResponse200PhoneNumbersItemVerificationType2Type0Strategy(d.pop("strategy"))

        attempts = d.pop("attempts")

        expire_at = d.pop("expire_at")

        unlock_user_response_200_phone_numbers_item_verification_type_2_type_0 = cls(
            status=status,
            strategy=strategy,
            attempts=attempts,
            expire_at=expire_at,
        )

        return unlock_user_response_200_phone_numbers_item_verification_type_2_type_0
