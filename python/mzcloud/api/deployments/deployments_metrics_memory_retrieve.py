from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.prometheus_metrics import PrometheusMetrics
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    period: float,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/deployments/{id}/metrics/memory/{period}".format(client.base_url, id=id, period=period)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
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
    id: str,
    period: float,
    *,
    client: AuthenticatedClient,
) -> Response[PrometheusMetrics]:
    """Retrieve memory line graph data (as a list of tuples (timestamps / utilization in %)) for a
    deployment.

    Args:
        id (str):
        period (float):

    Returns:
        Response[PrometheusMetrics]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    period: float,
    *,
    client: AuthenticatedClient,
) -> Optional[PrometheusMetrics]:
    """Retrieve memory line graph data (as a list of tuples (timestamps / utilization in %)) for a
    deployment.

    Args:
        id (str):
        period (float):

    Returns:
        Response[PrometheusMetrics]
    """

    return sync_detailed(
        id=id,
        period=period,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    period: float,
    *,
    client: AuthenticatedClient,
) -> Response[PrometheusMetrics]:
    """Retrieve memory line graph data (as a list of tuples (timestamps / utilization in %)) for a
    deployment.

    Args:
        id (str):
        period (float):

    Returns:
        Response[PrometheusMetrics]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    period: float,
    *,
    client: AuthenticatedClient,
) -> Optional[PrometheusMetrics]:
    """Retrieve memory line graph data (as a list of tuples (timestamps / utilization in %)) for a
    deployment.

    Args:
        id (str):
        period (float):

    Returns:
        Response[PrometheusMetrics]
    """

    return (
        await asyncio_detailed(
            id=id,
            period=period,
            client=client,
        )
    ).parsed
