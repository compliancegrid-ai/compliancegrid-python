"""HS code lookup — search, AI classification, reference data."""

from __future__ import annotations
from typing import Any, Optional


class HSCodes:
    def __init__(self, http: Any):
        self._http = http

    def search(self, query: str, limit: Optional[int] = None) -> dict:
        """Search HTS codes by keyword."""
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        return self._http.get("/v1/hs/search", params)

    def classify(self, description: str, destination_country: Optional[str] = None) -> dict:
        """AI-powered HS classification."""
        body: dict[str, Any] = {"description": description}
        if destination_country:
            body["destinationCountry"] = destination_country
        return self._http.post("/v1/hs/classify", body)

    def lookup(self, hts_number: str) -> dict:
        """Look up a specific HTS number."""
        return self._http.get(f"/v1/hs/lookup/{hts_number}")

    def sections(self) -> dict:
        """Get HTS sections overview."""
        return self._http.get("/v1/hs/reference/sections")

    def gri(self) -> dict:
        """Get General Rules of Interpretation."""
        return self._http.get("/v1/hs/reference/gri")

    def cache_stats(self) -> dict:
        """Get cache statistics."""
        return self._http.get("/v1/hs/cache-stats")
