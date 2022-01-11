from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.prometheus_metrics import PrometheusMetrics
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: str,
    period: float,
) -> Dict[str, Any]:
    url = "{}/api/deployments/{id}/metrics/cpu/{period}".format(client.base_url, id=id, period=period)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[PrometheusMetrics]:
    if response.status_code == 200:
        response_200 = PrometheusMetrics.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PrometheusMetrics]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    period: float,
) -> Response[PrometheusMetrics]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        period=period,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    period: float,
) -> Optional[PrometheusMetrics]:
    """Retrieve cpu line graph as a list of tuples (timestamps / utilization in %)) for a deployment."""

    return sync_detailed(
        client=client,
        id=id,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    period: float,
) -> Response[PrometheusMetrics]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        period=period,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    period: float,
) -> Optional[PrometheusMetrics]:
    """Retrieve cpu line graph as a list of tuples (timestamps / utilization in %)) for a deployment."""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            period=period,
        )
    ).parsed
