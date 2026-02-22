"""Core HTTP client and ComplianceGrid SDK entry point."""

from __future__ import annotations

from typing import Any, Optional

import httpx

from .resources.compliance import Compliance
from .resources.aes import AES
from .resources.hs import HSCodes
from .resources.firearms import Firearms
from .resources.pharma import Pharma
from .resources.financial import Financial
from .resources.aviation import Aviation
from .resources.maritime import Maritime
from .resources.business import Business
from .resources.legal import Legal
from .resources.fcc import FCC
from .resources.ai import AI


class ApiError(Exception):
    """Raised when the ComplianceGrid API returns a non-2xx response."""

    def __init__(self, status_code: int, code: str, message: str, response: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.response = response


class HttpClient:
    """Low-level HTTP client that handles auth and routing."""

    def __init__(self, api_key: str, base_url: Optional[str] = None, timeout: float = 30.0):
        is_sandbox = api_key.startswith("cg_sk_")
        self._base_url = base_url or (
            "https://sandbox.api.compliancegrid.ai" if is_sandbox else "https://api.compliancegrid.ai"
        )
        self._client = httpx.Client(
            base_url=self._base_url,
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
            },
            timeout=timeout,
        )

    def get(self, path: str, params: Optional[dict[str, Any]] = None) -> Any:
        """Send a GET request."""
        resp = self._client.get(path, params=params)
        return self._handle(resp)

    def post(self, path: str, json: Optional[dict[str, Any]] = None) -> Any:
        """Send a POST request."""
        resp = self._client.post(path, json=json)
        return self._handle(resp)

    def delete(self, path: str) -> Any:
        """Send a DELETE request."""
        resp = self._client.delete(path)
        return self._handle(resp)

    def _handle(self, resp: httpx.Response) -> Any:
        data = resp.json()
        if resp.status_code >= 400:
            error = data.get("error", {})
            code = error.get("code", error) if isinstance(error, dict) else str(error)
            message = error.get("message", str(data)) if isinstance(error, dict) else data.get("message", str(data))
            raise ApiError(resp.status_code, code, message, data)
        return data

    def close(self):
        self._client.close()


class ComplianceGrid:
    """
    Official ComplianceGrid Python SDK.

    Usage::

        from compliancegrid import ComplianceGrid

        cg = ComplianceGrid(api_key="cg_sk_your_sandbox_key")
        result = cg.compliance.screen_parties([{"name": "Acme Corp", "country": "CN"}])
        print(result["data"]["summary"])
    """

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self._http = HttpClient(api_key, base_url, timeout)
        self.compliance = Compliance(self._http)
        self.aes = AES(self._http)
        self.hs = HSCodes(self._http)
        self.firearms = Firearms(self._http)
        self.pharma = Pharma(self._http)
        self.financial = Financial(self._http)
        self.aviation = Aviation(self._http)
        self.maritime = Maritime(self._http)
        self.business = Business(self._http)
        self.legal = Legal(self._http)
        self.fcc = FCC(self._http)
        self.ai = AI(self._http)

    def close(self):
        """Close the underlying HTTP client."""
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
