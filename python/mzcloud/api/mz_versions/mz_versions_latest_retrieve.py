from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    track: Union[Unset, None, str] = "stable",
) -> Dict[str, Any]:
    url = "{}/api/mz-versions/latest".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["track"] = track

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    track: Union[Unset, None, str] = "stable",
) -> Response[str]:
    """Returns the latest version of Materialize.

    Args:
        track (Union[Unset, None, str]):  Default: 'stable'.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        client=client,
        track=track,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    track: Union[Unset, None, str] = "stable",
) -> Optional[str]:
    """Returns the latest version of Materialize.

    Args:
        track (Union[Unset, None, str]):  Default: 'stable'.

    Returns:
        Response[str]
    """

    return sync_detailed(
        client=client,
        track=track,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    track: Union[Unset, None, str] = "stable",
) -> Response[str]:
    """Returns the latest version of Materialize.

    Args:
        track (Union[Unset, None, str]):  Default: 'stable'.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        client=client,
        track=track,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    track: Union[Unset, None, str] = "stable",
) -> Optional[str]:
    """Returns the latest version of Materialize.

    Args:
        track (Union[Unset, None, str]):  Default: 'stable'.

    Returns:
        Response[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            track=track,
        )
    ).parsed
