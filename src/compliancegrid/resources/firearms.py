"""Firearms & explosives — ATF FFL search, verification, reference data."""

from __future__ import annotations
from typing import Any, Optional


class Firearms:
    def __init__(self, http: Any):
        self._http = http

    def search_ffl(
        self,
        ffl_number: Optional[str] = None,
        business_name: Optional[str] = None,
        license_name: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        zip_code: Optional[str] = None,
        license_type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> dict:
        """Search FFL holders by state, city, business name, etc."""
        body: dict[str, Any] = {}
        if ffl_number:
            body["fflNumber"] = ffl_number
        if business_name:
            body["businessName"] = business_name
        if license_name:
            body["licenseName"] = license_name
        if state:
            body["state"] = state
        if city:
            body["city"] = city
        if zip_code:
            body["zip"] = zip_code
        if license_type:
            body["licenseType"] = license_type
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/firearms/ffl/search", body)

    def verify_ffl(self, ffl_number: str) -> dict:
        """Verify a specific FFL number."""
        return self._http.get(f"/v1/firearms/ffl/verify/{ffl_number}")

    def parse_ffl(self, ffl_number: str) -> dict:
        """Parse an FFL number into its components."""
        return self._http.get(f"/v1/firearms/ffl/parse/{ffl_number}")

    def stats(self) -> dict:
        """Get FFL database statistics."""
        return self._http.get("/v1/firearms/ffl/stats")

    def ffl_types(self) -> dict:
        """Get FFL license type reference data."""
        return self._http.get("/v1/firearms/reference/ffl-types")

    def fel_types(self) -> dict:
        """Get FEL (Federal Explosives License) types."""
        return self._http.get("/v1/firearms/reference/fel-types")

    def regions(self) -> dict:
        """Get ATF regions."""
        return self._http.get("/v1/firearms/reference/regions")

    def states(self) -> dict:
        """Get state abbreviations."""
        return self._http.get("/v1/firearms/reference/states")
