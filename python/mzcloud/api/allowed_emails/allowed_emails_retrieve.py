from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Dict[str, Any]:
    url = "{}/api/allowed-emails/{email}".format(client.base_url, email=email)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[bool]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[bool]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Response[bool]:
    kwargs = _get_kwargs(
        client=client,
        email=email,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Optional[bool]:
    """Report whether the specified email address is allowed to sign up for
    Materialize Cloud."""

    return sync_detailed(
        client=client,
        email=email,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Response[bool]:
    kwargs = _get_kwargs(
        client=client,
        email=email,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Optional[bool]:
    """Report whether the specified email address is allowed to sign up for
    Materialize Cloud."""

    return (
        await asyncio_detailed(
            client=client,
            email=email,
        )
    ).parsed
