"""Professional & business — SAM.gov entity search."""

from __future__ import annotations
from typing import Any, Optional


class Business:
    def __init__(self, http: Any):
        self._http = http

    def search_sam(self, search: Optional[str] = None, uei_sam: Optional[str] = None, cage_code: Optional[str] = None, state: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search SAM.gov registered entities."""
        body: dict[str, Any] = {}
        if search:
            body["search"] = search
        if uei_sam:
            body["ueiSAM"] = uei_sam
        if cage_code:
            body["cageCode"] = cage_code
        if state:
            body["state"] = state
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/business/sam/search", body)

    def lookup_by_uei(self, uei: str) -> dict:
        """Look up a SAM.gov entity by UEI."""
        return self._http.get(f"/v1/business/sam/entity/{uei}")
