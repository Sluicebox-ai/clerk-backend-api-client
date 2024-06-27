from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_jwt_template_response_404_errors_item import GetJWTTemplateResponse404ErrorsItem
    from ..models.get_jwt_template_response_404_meta import GetJWTTemplateResponse404Meta


T = TypeVar("T", bound="GetJWTTemplateResponse404")


@_attrs_define
class GetJWTTemplateResponse404:
    """
    Attributes:
        errors (List['GetJWTTemplateResponse404ErrorsItem']):
        meta (Union[Unset, GetJWTTemplateResponse404Meta]):
    """

    errors: List["GetJWTTemplateResponse404ErrorsItem"]
    meta: Union[Unset, "GetJWTTemplateResponse404Meta"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_jwt_template_response_404_errors_item import GetJWTTemplateResponse404ErrorsItem
        from ..models.get_jwt_template_response_404_meta import GetJWTTemplateResponse404Meta

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = GetJWTTemplateResponse404ErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, GetJWTTemplateResponse404Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetJWTTemplateResponse404Meta.from_dict(_meta)

        get_jwt_template_response_404 = cls(
            errors=errors,
            meta=meta,
        )

        get_jwt_template_response_404.additional_properties = d
        return get_jwt_template_response_404

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties