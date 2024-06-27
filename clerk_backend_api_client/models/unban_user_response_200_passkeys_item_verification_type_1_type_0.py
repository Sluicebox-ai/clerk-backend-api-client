from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.unban_user_response_200_passkeys_item_verification_type_1_type_0_nonce import (
    UnbanUserResponse200PasskeysItemVerificationType1Type0Nonce,
)
from ..models.unban_user_response_200_passkeys_item_verification_type_1_type_0_status import (
    UnbanUserResponse200PasskeysItemVerificationType1Type0Status,
)
from ..models.unban_user_response_200_passkeys_item_verification_type_1_type_0_strategy import (
    UnbanUserResponse200PasskeysItemVerificationType1Type0Strategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnbanUserResponse200PasskeysItemVerificationType1Type0")


@_attrs_define
class UnbanUserResponse200PasskeysItemVerificationType1Type0:
    """
    Attributes:
        status (UnbanUserResponse200PasskeysItemVerificationType1Type0Status):
        strategy (UnbanUserResponse200PasskeysItemVerificationType1Type0Strategy):
        nonce (Union[Unset, UnbanUserResponse200PasskeysItemVerificationType1Type0Nonce]):
        attempts (Union[None, Unset, int]):
        expire_at (Union[None, Unset, int]):
    """

    status: UnbanUserResponse200PasskeysItemVerificationType1Type0Status
    strategy: UnbanUserResponse200PasskeysItemVerificationType1Type0Strategy
    nonce: Union[Unset, UnbanUserResponse200PasskeysItemVerificationType1Type0Nonce] = UNSET
    attempts: Union[None, Unset, int] = UNSET
    expire_at: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        strategy = self.strategy.value

        nonce: Union[Unset, str] = UNSET
        if not isinstance(self.nonce, Unset):
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
            }
        )
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if expire_at is not UNSET:
            field_dict["expire_at"] = expire_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = UnbanUserResponse200PasskeysItemVerificationType1Type0Status(d.pop("status"))

        strategy = UnbanUserResponse200PasskeysItemVerificationType1Type0Strategy(d.pop("strategy"))

        _nonce = d.pop("nonce", UNSET)
        nonce: Union[Unset, UnbanUserResponse200PasskeysItemVerificationType1Type0Nonce]
        if isinstance(_nonce, Unset):
            nonce = UNSET
        else:
            nonce = UnbanUserResponse200PasskeysItemVerificationType1Type0Nonce(_nonce)

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

        unban_user_response_200_passkeys_item_verification_type_1_type_0 = cls(
            status=status,
            strategy=strategy,
            nonce=nonce,
            attempts=attempts,
            expire_at=expire_at,
        )

        return unban_user_response_200_passkeys_item_verification_type_1_type_0