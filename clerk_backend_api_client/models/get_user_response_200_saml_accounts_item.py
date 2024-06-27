from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.get_user_response_200_saml_accounts_item_object import GetUserResponse200SamlAccountsItemObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_user_response_200_saml_accounts_item_public_metadata import (
        GetUserResponse200SamlAccountsItemPublicMetadata,
    )
    from ..models.get_user_response_200_saml_accounts_item_verification_type_0 import (
        GetUserResponse200SamlAccountsItemVerificationType0,
    )
    from ..models.get_user_response_200_saml_accounts_item_verification_type_1 import (
        GetUserResponse200SamlAccountsItemVerificationType1,
    )
    from ..models.get_user_response_200_saml_accounts_item_verification_type_2_type_0 import (
        GetUserResponse200SamlAccountsItemVerificationType2Type0,
    )
    from ..models.get_user_response_200_saml_accounts_item_verification_type_2_type_1 import (
        GetUserResponse200SamlAccountsItemVerificationType2Type1,
    )
    from ..models.get_user_response_200_saml_accounts_item_verification_type_3_type_0 import (
        GetUserResponse200SamlAccountsItemVerificationType3Type0,
    )
    from ..models.get_user_response_200_saml_accounts_item_verification_type_3_type_1 import (
        GetUserResponse200SamlAccountsItemVerificationType3Type1,
    )


T = TypeVar("T", bound="GetUserResponse200SamlAccountsItem")


@_attrs_define
class GetUserResponse200SamlAccountsItem:
    """
    Attributes:
        id (str):
        object_ (GetUserResponse200SamlAccountsItemObject): String representing the object's type. Objects of the same
            type share the same value.
        provider (str):
        active (bool):
        email_address (str):
        verification (Union['GetUserResponse200SamlAccountsItemVerificationType0',
            'GetUserResponse200SamlAccountsItemVerificationType1',
            'GetUserResponse200SamlAccountsItemVerificationType2Type0',
            'GetUserResponse200SamlAccountsItemVerificationType2Type1',
            'GetUserResponse200SamlAccountsItemVerificationType3Type0',
            'GetUserResponse200SamlAccountsItemVerificationType3Type1']):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        provider_user_id (Union[None, Unset, str]):
        public_metadata (Union[Unset, GetUserResponse200SamlAccountsItemPublicMetadata]):
    """

    id: str
    object_: GetUserResponse200SamlAccountsItemObject
    provider: str
    active: bool
    email_address: str
    verification: Union[
        "GetUserResponse200SamlAccountsItemVerificationType0",
        "GetUserResponse200SamlAccountsItemVerificationType1",
        "GetUserResponse200SamlAccountsItemVerificationType2Type0",
        "GetUserResponse200SamlAccountsItemVerificationType2Type1",
        "GetUserResponse200SamlAccountsItemVerificationType3Type0",
        "GetUserResponse200SamlAccountsItemVerificationType3Type1",
    ]
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    provider_user_id: Union[None, Unset, str] = UNSET
    public_metadata: Union[Unset, "GetUserResponse200SamlAccountsItemPublicMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_user_response_200_saml_accounts_item_verification_type_0 import (
            GetUserResponse200SamlAccountsItemVerificationType0,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_1 import (
            GetUserResponse200SamlAccountsItemVerificationType1,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_2_type_0 import (
            GetUserResponse200SamlAccountsItemVerificationType2Type0,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_2_type_1 import (
            GetUserResponse200SamlAccountsItemVerificationType2Type1,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_3_type_0 import (
            GetUserResponse200SamlAccountsItemVerificationType3Type0,
        )

        id = self.id

        object_ = self.object_.value

        provider = self.provider

        active = self.active

        email_address = self.email_address

        verification: Dict[str, Any]
        if isinstance(self.verification, GetUserResponse200SamlAccountsItemVerificationType0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserResponse200SamlAccountsItemVerificationType1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserResponse200SamlAccountsItemVerificationType2Type0):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserResponse200SamlAccountsItemVerificationType2Type1):
            verification = self.verification.to_dict()
        elif isinstance(self.verification, GetUserResponse200SamlAccountsItemVerificationType3Type0):
            verification = self.verification.to_dict()
        else:
            verification = self.verification.to_dict()

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        provider_user_id: Union[None, Unset, str]
        if isinstance(self.provider_user_id, Unset):
            provider_user_id = UNSET
        else:
            provider_user_id = self.provider_user_id

        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "provider": provider,
                "active": active,
                "email_address": email_address,
                "verification": verification,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if provider_user_id is not UNSET:
            field_dict["provider_user_id"] = provider_user_id
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_user_response_200_saml_accounts_item_public_metadata import (
            GetUserResponse200SamlAccountsItemPublicMetadata,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_0 import (
            GetUserResponse200SamlAccountsItemVerificationType0,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_1 import (
            GetUserResponse200SamlAccountsItemVerificationType1,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_2_type_0 import (
            GetUserResponse200SamlAccountsItemVerificationType2Type0,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_2_type_1 import (
            GetUserResponse200SamlAccountsItemVerificationType2Type1,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_3_type_0 import (
            GetUserResponse200SamlAccountsItemVerificationType3Type0,
        )
        from ..models.get_user_response_200_saml_accounts_item_verification_type_3_type_1 import (
            GetUserResponse200SamlAccountsItemVerificationType3Type1,
        )

        d = src_dict.copy()
        id = d.pop("id")

        object_ = GetUserResponse200SamlAccountsItemObject(d.pop("object"))

        provider = d.pop("provider")

        active = d.pop("active")

        email_address = d.pop("email_address")

        def _parse_verification(
            data: object,
        ) -> Union[
            "GetUserResponse200SamlAccountsItemVerificationType0",
            "GetUserResponse200SamlAccountsItemVerificationType1",
            "GetUserResponse200SamlAccountsItemVerificationType2Type0",
            "GetUserResponse200SamlAccountsItemVerificationType2Type1",
            "GetUserResponse200SamlAccountsItemVerificationType3Type0",
            "GetUserResponse200SamlAccountsItemVerificationType3Type1",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = GetUserResponse200SamlAccountsItemVerificationType0.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_1 = GetUserResponse200SamlAccountsItemVerificationType1.from_dict(data)

                return verification_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2_type_0 = GetUserResponse200SamlAccountsItemVerificationType2Type0.from_dict(data)

                return verification_type_2_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_2_type_1 = GetUserResponse200SamlAccountsItemVerificationType2Type1.from_dict(data)

                return verification_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_3_type_0 = GetUserResponse200SamlAccountsItemVerificationType3Type0.from_dict(data)

                return verification_type_3_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_3_type_1 = GetUserResponse200SamlAccountsItemVerificationType3Type1.from_dict(data)

            return verification_type_3_type_1

        verification = _parse_verification(d.pop("verification"))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_provider_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_user_id = _parse_provider_user_id(d.pop("provider_user_id", UNSET))

        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, GetUserResponse200SamlAccountsItemPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = GetUserResponse200SamlAccountsItemPublicMetadata.from_dict(_public_metadata)

        get_user_response_200_saml_accounts_item = cls(
            id=id,
            object_=object_,
            provider=provider,
            active=active,
            email_address=email_address,
            verification=verification,
            first_name=first_name,
            last_name=last_name,
            provider_user_id=provider_user_id,
            public_metadata=public_metadata,
        )

        return get_user_response_200_saml_accounts_item
