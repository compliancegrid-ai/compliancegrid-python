"""Maritime & port security — vessel search, C-TPAT partner lookup."""

from __future__ import annotations
from typing import Any, Optional


class Maritime:
    def __init__(self, http: Any):
        self._http = http

    def search_vessels(self, name: Optional[str] = None, imo: Optional[str] = None, mmsi: Optional[str] = None, flag: Optional[str] = None, vessel_type: Optional[str] = None, limit: Optional[int] = None) -> dict:
        """Search vessels by name, IMO, MMSI, flag, or type."""
        body: dict[str, Any] = {}
        if name:
            body["name"] = name
        if imo:
            body["imo"] = imo
        if mmsi:
            body["mmsi"] = mmsi
        if flag:
            body["flag"] = flag
        if vessel_type:
            body["vesselType"] = vessel_type
        if limit is not None:
            body["limit"] = limit
        return self._http.post("/v1/maritime/vessels", body)

    def lookup_by_imo(self, imo: str) -> dict:
        """Look up a vessel by IMO number."""
        return self._http.get(f"/v1/maritime/vessels/imo/{imo}")

    def search_ctpat(self, company_name: Optional[str] = None, svi_number: Optional[str] = None, tier: Optional[str] = None, limit: Optional[int] = None) -> dict:
        """Search C-TPAT certified partners."""
        body: dict[str, Any] = {}
        if company_name:
            body["companyName"] = company_name
        if svi_number:
            body["sviNumber"] = svi_number
        if tier:
            body["tier"] = tier
        if limit is not None:
            body["limit"] = limit
        return self._http.post("/v1/maritime/ctpat", body)
