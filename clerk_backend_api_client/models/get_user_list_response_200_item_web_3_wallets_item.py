from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_user_list_response_200_item_web_3_wallets_item_object import (
    GetUserListResponse200ItemWeb3WalletsItemObject,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_0 import (
        GetUserListResponse200ItemWeb3WalletsItemVerificationType0,
    )
    from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_1 import (
        GetUserListResponse200ItemWeb3WalletsItemVerificationType1,
    )
    from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_2_type_0 import (
        GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0,
    )
    from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_2_type_1 import (
        GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1,
    )
    from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_3_type_0 import (
        GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0,
    )
    from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_3_type_1 import (
        GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type1,
    )


T = TypeVar("T", bound="GetUserListResponse200ItemWeb3WalletsItem")


@_attrs_define
class GetUserListResponse200ItemWeb3WalletsItem:
    """
    Attributes:
        object_ (GetUserListResponse200ItemWeb3WalletsItemObject): String representing the object's type. Objects of the
            same type share the same value.
        web3_wallet (str):
        verification (Union['GetUserListResponse200ItemWeb3WalletsItemVerificationType0',
            'GetUserListResponse200ItemWeb3WalletsItemVerificationType1',
            'GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0',
            'GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1',
            'GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0',
            'GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type1']):
        created_at (int): Unix timestamp of creation
        updated_at (int): Unix timestamp of creation
        id (Union[Unset, str]):
    """

    object_: GetUserListResponse200ItemWeb3WalletsItemObject
    web3_wallet: str
    verification: Union[
        "GetUserListResponse200ItemWeb3WalletsItemVerificationType0",
        "GetUserListResponse200ItemWeb3WalletsItemVerificationType1",
        "GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0",
        "GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1",
        "GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0",
        "GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type1",
    ]
    created_at: int
    updated_at: int
    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_0 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType0,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_1 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType1,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_2_type_0 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_2_type_1 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_3_type_0 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0,
        )

        object_ = self.object_.value

        web3_wallet = self.web3_wallet

        verification: Dict[str, Any]
        if isinstance(self.verification, GetUserListResponse200ItemWeb3WalletsItemVerificationType0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserListResponse200ItemWeb3WalletsItemVerificationType1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0):
            verification = self.verification.to_dict()
        else:
            verification = self.verification.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "web3_wallet": web3_wallet,
                "verification": verification,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_0 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType0,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_1 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType1,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_2_type_0 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_2_type_1 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_3_type_0 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0,
        )
        from ..models.get_user_list_response_200_item_web_3_wallets_item_verification_type_3_type_1 import (
            GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type1,
        )

        d = src_dict.copy()
        object_ = GetUserListResponse200ItemWeb3WalletsItemObject(d.pop("object"))

        web3_wallet = d.pop("web3_wallet")

        def _parse_verification(
            data: object,
        ) -> Union[
            "GetUserListResponse200ItemWeb3WalletsItemVerificationType0",
            "GetUserListResponse200ItemWeb3WalletsItemVerificationType1",
            "GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0",
            "GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1",
            "GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0",
            "GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type1",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = GetUserListResponse200ItemWeb3WalletsItemVerificationType0.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_1 = GetUserListResponse200ItemWeb3WalletsItemVerificationType1.from_dict(data)

                return verification_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2_type_0 = GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type0.from_dict(
                    data
                )

                return verification_type_2_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2_type_1 = GetUserListResponse200ItemWeb3WalletsItemVerificationType2Type1.from_dict(
                    data
                )

                return verification_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_0 = GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type0.from_dict(
                    data
                )

                return verification_type_3_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_3_type_1 = GetUserListResponse200ItemWeb3WalletsItemVerificationType3Type1.from_dict(data)

            return verification_type_3_type_1

        verification = _parse_verification(d.pop("verification"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        get_user_list_response_200_item_web_3_wallets_item = cls(
            object_=object_,
            web3_wallet=web3_wallet,
            verification=verification,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
        )

        return get_user_list_response_200_item_web_3_wallets_item
