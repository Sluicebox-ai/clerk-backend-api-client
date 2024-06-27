from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verify_totp_body import VerifyTOTPBody
from ...models.verify_totp_response_200 import VerifyTOTPResponse200
from ...models.verify_totp_response_500 import VerifyTOTPResponse500
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: VerifyTOTPBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/users/{user_id}/verify_totp",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VerifyTOTPResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = VerifyTOTPResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]:
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
    body: VerifyTOTPBody,
) -> Response[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]:
    """Verify a TOTP or backup code for a user

     Verify that the provided TOTP or backup code is valid for the user.
    Verifying a backup code will result it in being consumed (i.e. it will
    become invalid).
    Useful for custom auth flows and re-verification.

    Args:
        user_id (str):
        body (VerifyTOTPBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTOTPBody,
) -> Optional[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]:
    """Verify a TOTP or backup code for a user

     Verify that the provided TOTP or backup code is valid for the user.
    Verifying a backup code will result it in being consumed (i.e. it will
    become invalid).
    Useful for custom auth flows and re-verification.

    Args:
        user_id (str):
        body (VerifyTOTPBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTOTPBody,
) -> Response[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]:
    """Verify a TOTP or backup code for a user

     Verify that the provided TOTP or backup code is valid for the user.
    Verifying a backup code will result it in being consumed (i.e. it will
    become invalid).
    Useful for custom auth flows and re-verification.

    Args:
        user_id (str):
        body (VerifyTOTPBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTOTPBody,
) -> Optional[Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]]:
    """Verify a TOTP or backup code for a user

     Verify that the provided TOTP or backup code is valid for the user.
    Verifying a backup code will result it in being consumed (i.e. it will
    become invalid).
    Useful for custom auth flows and re-verification.

    Args:
        user_id (str):
        body (VerifyTOTPBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VerifyTOTPResponse200, VerifyTOTPResponse500]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
