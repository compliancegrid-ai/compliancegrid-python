"""Pharma & controlled substances — DEA, FDA drugs, shortages, recalls."""

from __future__ import annotations
from typing import Any, Optional


class Pharma:
    def __init__(self, http: Any):
        self._http = http

    def lookup_dea(self, dea_number: str) -> dict:
        """Look up a DEA registration by number."""
        return self._http.get(f"/v1/pharma/dea/lookup/{dea_number}")

    def search_dea(self, name: Optional[str] = None, state: Optional[str] = None, business_activity: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search DEA registrations."""
        body: dict[str, Any] = {}
        if name:
            body["name"] = name
        if state:
            body["state"] = state
        if business_activity:
            body["businessActivity"] = business_activity
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/pharma/dea/search", body)

    def validate_dea(self, dea_number: str) -> dict:
        """Validate a DEA number checksum."""
        return self._http.get(f"/v1/pharma/dea/validate/{dea_number}")

    def search_drugs(self, search: str, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search FDA drug database."""
        body: dict[str, Any] = {"search": search}
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/pharma/fda/drug/search", body)

    def lookup_ndc(self, ndc: str) -> dict:
        """Look up an NDC code."""
        return self._http.get(f"/v1/pharma/fda/drug/ndc/{ndc}")

    def search_shortages(self, search: str, limit: Optional[int] = None) -> dict:
        """Search FDA drug shortages."""
        body: dict[str, Any] = {"search": search}
        if limit is not None:
            body["limit"] = limit
        return self._http.post("/v1/pharma/fda/shortages", body)

    def search_recalls(self, search: str, classification: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search FDA drug recalls."""
        body: dict[str, Any] = {"search": search}
        if classification:
            body["classification"] = classification
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/pharma/fda/recalls", body)

    def dea_schedules(self) -> dict:
        """Get DEA schedule reference data."""
        return self._http.get("/v1/pharma/reference/dea-schedules")

    def business_activities(self) -> dict:
        """Get DEA business activity codes."""
        return self._http.get("/v1/pharma/reference/business-activities")
