"""FCC licensing — ULS license search."""

from __future__ import annotations
from typing import Any, Optional


class FCC:
    def __init__(self, http: Any):
        self._http = http

    def search_licenses(self, search: Optional[str] = None, call_sign: Optional[str] = None, frn: Optional[str] = None, radio_service: Optional[str] = None, state: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search FCC ULS licenses."""
        body: dict[str, Any] = {}
        if search:
            body["search"] = search
        if call_sign:
            body["callSign"] = call_sign
        if frn:
            body["frn"] = frn
        if radio_service:
            body["radioService"] = radio_service
        if state:
            body["state"] = state
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/fcc/licenses", body)

    def lookup_by_call_sign(self, call_sign: str) -> dict:
        """Look up a license by call sign."""
        return self._http.get(f"/v1/fcc/licenses/callsign/{call_sign}")
