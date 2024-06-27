from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.ban_user_response_200_web_3_wallets_item_verification_type_2_type_0_nonce import (
    BanUserResponse200Web3WalletsItemVerificationType2Type0Nonce,
)
from ..models.ban_user_response_200_web_3_wallets_item_verification_type_2_type_0_status import (
    BanUserResponse200Web3WalletsItemVerificationType2Type0Status,
)
from ..models.ban_user_response_200_web_3_wallets_item_verification_type_2_type_0_strategy import (
    BanUserResponse200Web3WalletsItemVerificationType2Type0Strategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BanUserResponse200Web3WalletsItemVerificationType2Type0")


@_attrs_define
class BanUserResponse200Web3WalletsItemVerificationType2Type0:
    """
    Attributes:
        status (BanUserResponse200Web3WalletsItemVerificationType2Type0Status):
        strategy (BanUserResponse200Web3WalletsItemVerificationType2Type0Strategy):
        nonce (BanUserResponse200Web3WalletsItemVerificationType2Type0Nonce):
        attempts (Union[None, Unset, int]):
        expire_at (Union[None, Unset, int]):
    """

    status: BanUserResponse200Web3WalletsItemVerificationType2Type0Status
    strategy: BanUserResponse200Web3WalletsItemVerificationType2Type0Strategy
    nonce: BanUserResponse200Web3WalletsItemVerificationType2Type0Nonce
    attempts: Union[None, Unset, int] = UNSET
    expire_at: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        strategy = self.strategy.value

        nonce = self.nonce.value

        attempts: Union[None, Unset, int]
        if isinstance(self.attempts, Unset):
            attempts = UNSET
        else:
            attempts = self.attempts

        expire_at: Union[None, Unset, int]
        if isinstance(self.expire_at, Unset):
            expire_at = UNSET
        else:
            expire_at = self.expire_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "strategy": strategy,
                "nonce": nonce,
            }
        )
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if expire_at is not UNSET:
            field_dict["expire_at"] = expire_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = BanUserResponse200Web3WalletsItemVerificationType2Type0Status(d.pop("status"))

        strategy = BanUserResponse200Web3WalletsItemVerificationType2Type0Strategy(d.pop("strategy"))

        nonce = BanUserResponse200Web3WalletsItemVerificationType2Type0Nonce(d.pop("nonce"))

        def _parse_attempts(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        attempts = _parse_attempts(d.pop("attempts", UNSET))

        def _parse_expire_at(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        expire_at = _parse_expire_at(d.pop("expire_at", UNSET))

        ban_user_response_200_web_3_wallets_item_verification_type_2_type_0 = cls(
            status=status,
            strategy=strategy,
            nonce=nonce,
            attempts=attempts,
            expire_at=expire_at,
        )

        return ban_user_response_200_web_3_wallets_item_verification_type_2_type_0