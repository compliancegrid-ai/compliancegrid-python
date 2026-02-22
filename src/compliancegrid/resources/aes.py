"""AES filing — validation, preparation, submission."""

from __future__ import annotations
from typing import Any, Optional


class AES:
    def __init__(self, http: Any):
        self._http = http

    def validate(self, payload: dict[str, Any]) -> dict:
        """Validate an AES filing payload."""
        return self._http.post("/v1/aes/validate", payload)

    def prepare(self, payload: dict[str, Any]) -> dict:
        """Prepare an AES filing payload for submission."""
        return self._http.post("/v1/aes/prepare", payload)

    def filing_required(self, destination_country: str, value: float, schedule_b: Optional[str] = None) -> dict:
        """Determine if AES filing is required."""
        body: dict[str, Any] = {"destinationCountry": destination_country, "value": value}
        if schedule_b:
            body["scheduleB"] = schedule_b
        return self._http.post("/v1/aes/filing-required", body)

    def create_filing(self, payload: dict[str, Any]) -> dict:
        """Create a draft AES filing."""
        return self._http.post("/v1/aes/filing", payload)

    def get_filing(self, filing_id: str) -> dict:
        """Get a filing by ID."""
        return self._http.get(f"/v1/aes/filing/{filing_id}")

    def list_filings(self, status: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """List all filings."""
        params: dict[str, Any] = {}
        if status:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._http.get("/v1/aes/filings", params or None)
