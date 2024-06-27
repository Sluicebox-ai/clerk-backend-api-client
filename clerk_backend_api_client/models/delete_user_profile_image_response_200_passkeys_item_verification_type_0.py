from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.delete_user_profile_image_response_200_passkeys_item_verification_type_0_nonce import (
    DeleteUserProfileImageResponse200PasskeysItemVerificationType0Nonce,
)
from ..models.delete_user_profile_image_response_200_passkeys_item_verification_type_0_status import (
    DeleteUserProfileImageResponse200PasskeysItemVerificationType0Status,
)
from ..models.delete_user_profile_image_response_200_passkeys_item_verification_type_0_strategy import (
    DeleteUserProfileImageResponse200PasskeysItemVerificationType0Strategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteUserProfileImageResponse200PasskeysItemVerificationType0")


@_attrs_define
class DeleteUserProfileImageResponse200PasskeysItemVerificationType0:
    """
    Attributes:
        status (DeleteUserProfileImageResponse200PasskeysItemVerificationType0Status):
        strategy (DeleteUserProfileImageResponse200PasskeysItemVerificationType0Strategy):
        nonce (Union[Unset, DeleteUserProfileImageResponse200PasskeysItemVerificationType0Nonce]):
        attempts (Union[None, Unset, int]):
        expire_at (Union[None, Unset, int]):
    """

    status: DeleteUserProfileImageResponse200PasskeysItemVerificationType0Status
    strategy: DeleteUserProfileImageResponse200PasskeysItemVerificationType0Strategy
    nonce: Union[Unset, DeleteUserProfileImageResponse200PasskeysItemVerificationType0Nonce] = UNSET
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
        status = DeleteUserProfileImageResponse200PasskeysItemVerificationType0Status(d.pop("status"))

        strategy = DeleteUserProfileImageResponse200PasskeysItemVerificationType0Strategy(d.pop("strategy"))

        _nonce = d.pop("nonce", UNSET)
        nonce: Union[Unset, DeleteUserProfileImageResponse200PasskeysItemVerificationType0Nonce]
        if isinstance(_nonce, Unset):
            nonce = UNSET
        else:
            nonce = DeleteUserProfileImageResponse200PasskeysItemVerificationType0Nonce(_nonce)

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

        delete_user_profile_image_response_200_passkeys_item_verification_type_0 = cls(
            status=status,
            strategy=strategy,
            nonce=nonce,
            attempts=attempts,
            expire_at=expire_at,
        )

        return delete_user_profile_image_response_200_passkeys_item_verification_type_0
