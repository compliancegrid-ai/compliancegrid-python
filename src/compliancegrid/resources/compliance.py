"""Export compliance — screening, prohibited goods, export license, HS classification."""

from __future__ import annotations
from typing import Any, Optional


class Compliance:
    def __init__(self, http: Any):
        self._http = http

    def screen_parties(self, parties: list[dict[str, Any]]) -> dict:
        """Screen parties against OFAC SDN, BIS Entity List, DPL, ITAR, and more."""
        return self._http.post("/v1/compliance/restricted-party-screening", {"parties": parties})

    def search_screening_list(self, query: str) -> dict:
        """Search the consolidated screening list."""
        return self._http.get("/v1/compliance/search", {"query": query})

    def check_prohibited_goods(self, item: str, destination_country: str, origin_country: Optional[str] = None) -> dict:
        """Check if goods are prohibited for a destination."""
        body: dict[str, Any] = {"item": item, "destinationCountry": destination_country}
        if origin_country:
            body["originCountry"] = origin_country
        return self._http.post("/v1/compliance/prohibited-goods", body)

    def classify_hs(self, description: str, destination_country: Optional[str] = None) -> dict:
        """AI-powered HS classification."""
        body: dict[str, Any] = {"description": description}
        if destination_country:
            body["destinationCountry"] = destination_country
        return self._http.post("/v1/compliance/hs-classification", body)

    def description_guidance(self, description: str) -> dict:
        """Get guidance on improving product descriptions for customs."""
        return self._http.post("/v1/compliance/description-guidance", {"description": description})

    def check_export_license(self, item: str, destination_country: str, end_use: Optional[str] = None, eccn: Optional[str] = None) -> dict:
        """Determine if an export license is required."""
        body: dict[str, Any] = {"item": item, "destinationCountry": destination_country}
        if end_use:
            body["endUse"] = end_use
        if eccn:
            body["eccn"] = eccn
        return self._http.post("/v1/compliance/export-license", body)
