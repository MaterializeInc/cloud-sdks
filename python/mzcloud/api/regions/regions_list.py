from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.supported_cloud_region import SupportedCloudRegion
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    provider_name: str,
) -> Dict[str, Any]:
    url = "{}/api/regions/{providerName}".format(client.base_url, providerName=provider_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[SupportedCloudRegion]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SupportedCloudRegion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[SupportedCloudRegion]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider_name: str,
) -> Response[List[SupportedCloudRegion]]:
    kwargs = _get_kwargs(
        client=client,
        provider_name=provider_name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    provider_name: str,
) -> Optional[List[SupportedCloudRegion]]:
    """ """

    return sync_detailed(
        client=client,
        provider_name=provider_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider_name: str,
) -> Response[List[SupportedCloudRegion]]:
    kwargs = _get_kwargs(
        client=client,
        provider_name=provider_name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider_name: str,
) -> Optional[List[SupportedCloudRegion]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            provider_name=provider_name,
        )
    ).parsed