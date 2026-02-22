"""Legal & exclusions — OIG LEIE excluded individuals/entities."""

from __future__ import annotations
from typing import Any, Optional


class Legal:
    def __init__(self, http: Any):
        self._http = http

    def search_oig(self, last_name: Optional[str] = None, first_name: Optional[str] = None, business_name: Optional[str] = None, npi: Optional[str] = None, state: Optional[str] = None, exclusion_type: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search OIG LEIE excluded individuals/entities."""
        body: dict[str, Any] = {}
        if last_name:
            body["lastName"] = last_name
        if first_name:
            body["firstName"] = first_name
        if business_name:
            body["businessName"] = business_name
        if npi:
            body["npi"] = npi
        if state:
            body["state"] = state
        if exclusion_type:
            body["exclusionType"] = exclusion_type
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/legal/oig/search", body)

    def check_npi(self, npi: str) -> dict:
        """Quick NPI exclusion check."""
        return self._http.get(f"/v1/legal/oig/check/{npi}")
