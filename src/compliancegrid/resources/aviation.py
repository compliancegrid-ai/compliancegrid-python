"""Aviation & transport — FAA aircraft registry, FMCSA carrier safety."""

from __future__ import annotations
from typing import Any, Optional


class Aviation:
    def __init__(self, http: Any):
        self._http = http

    def search_aircraft(self, n_number: Optional[str] = None, registrant_name: Optional[str] = None, manufacturer: Optional[str] = None, model: Optional[str] = None, state: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search FAA aircraft registry."""
        body: dict[str, Any] = {}
        if n_number:
            body["nNumber"] = n_number
        if registrant_name:
            body["registrantName"] = registrant_name
        if manufacturer:
            body["manufacturer"] = manufacturer
        if model:
            body["model"] = model
        if state:
            body["state"] = state
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/aviation/faa/aircraft/search", body)

    def lookup_by_n_number(self, n_number: str) -> dict:
        """Look up aircraft by N-Number."""
        return self._http.get(f"/v1/aviation/faa/aircraft/{n_number}")

    def lookup_carrier(self, dot_number: str) -> dict:
        """Look up FMCSA carrier by DOT number."""
        return self._http.get(f"/v1/aviation/fmcsa/carrier/{dot_number}")

    def search_carriers(self, name: Optional[str] = None, state: Optional[str] = None, limit: Optional[int] = None) -> dict:
        """Search FMCSA carriers."""
        body: dict[str, Any] = {}
        if name:
            body["name"] = name
        if state:
            body["state"] = state
        if limit is not None:
            body["limit"] = limit
        return self._http.post("/v1/aviation/fmcsa/search", body)
