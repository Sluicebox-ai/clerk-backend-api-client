from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disable_mfa_response_200 import DisableMFAResponse200
from ...models.disable_mfa_response_404 import DisableMFAResponse404
from ...models.disable_mfa_response_500 import DisableMFAResponse500
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/users/{user_id}/mfa",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DisableMFAResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = DisableMFAResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DisableMFAResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]:
    """Disable a user's MFA methods

     Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at
    once.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]:
    """Disable a user's MFA methods

     Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at
    once.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]:
    """Disable a user's MFA methods

     Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at
    once.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]]:
    """Disable a user's MFA methods

     Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at
    once.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DisableMFAResponse200, DisableMFAResponse404, DisableMFAResponse500]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
