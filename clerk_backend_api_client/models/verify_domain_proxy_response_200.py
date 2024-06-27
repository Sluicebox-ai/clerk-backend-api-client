from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.verify_domain_proxy_response_200_object import VerifyDomainProxyResponse200Object

T = TypeVar("T", bound="VerifyDomainProxyResponse200")


@_attrs_define
class VerifyDomainProxyResponse200:
    """
    Attributes:
        object_ (VerifyDomainProxyResponse200Object):
        id (str):
        domain_id (str):
        last_run_at (int):
        proxy_url (str):
        successful (bool):
        created_at (int):
        updated_at (int):
    """

    object_: VerifyDomainProxyResponse200Object
    id: str
    domain_id: str
    last_run_at: int
    proxy_url: str
    successful: bool
    created_at: int
    updated_at: int

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        domain_id = self.domain_id

        last_run_at = self.last_run_at

        proxy_url = self.proxy_url

        successful = self.successful

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "domain_id": domain_id,
                "last_run_at": last_run_at,
                "proxy_url": proxy_url,
                "successful": successful,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = VerifyDomainProxyResponse200Object(d.pop("object"))

        id = d.pop("id")

        domain_id = d.pop("domain_id")

        last_run_at = d.pop("last_run_at")

        proxy_url = d.pop("proxy_url")

        successful = d.pop("successful")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        verify_domain_proxy_response_200 = cls(
            object_=object_,
            id=id,
            domain_id=domain_id,
            last_run_at=last_run_at,
            proxy_url=proxy_url,
            successful=successful,
            created_at=created_at,
            updated_at=updated_at,
        )

        return verify_domain_proxy_response_200
