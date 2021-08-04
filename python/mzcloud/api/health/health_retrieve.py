from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET




def _get_kwargs(
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/api/health".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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

) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

