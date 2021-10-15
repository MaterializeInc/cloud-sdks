from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: str,
    previous: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/deployments/{id}/logs".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "previous": previous,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    previous: Union[Unset, bool] = False,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        previous=previous,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    previous: Union[Unset, bool] = False,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        previous=previous,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
