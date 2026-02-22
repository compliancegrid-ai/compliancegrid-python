"""Financial & securities — SEC EDGAR, FDIC BankFind, FINRA BrokerCheck."""

from __future__ import annotations
from typing import Any, Optional


class Financial:
    def __init__(self, http: Any):
        self._http = http

    def search_sec(self, query: str) -> dict:
        """Search SEC EDGAR companies."""
        return self._http.get("/v1/financial/sec/search", {"q": query})

    def get_filings(self, cik: str, form_type: Optional[str] = None) -> dict:
        """Get SEC filings for a company by CIK."""
        params: dict[str, Any] = {}
        if form_type:
            params["form"] = form_type
        return self._http.get(f"/v1/financial/sec/filings/{cik}", params or None)

    def search_fdic(self, search: Optional[str] = None, state: Optional[str] = None, city: Optional[str] = None, active: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> dict:
        """Search FDIC-insured institutions."""
        body: dict[str, Any] = {}
        if search:
            body["search"] = search
        if state:
            body["state"] = state
        if city:
            body["city"] = city
        if active is not None:
            body["active"] = active
        if limit is not None:
            body["limit"] = limit
        if offset is not None:
            body["offset"] = offset
        return self._http.post("/v1/financial/fdic/search", body)

    def lookup_fdic(self, cert_number: str) -> dict:
        """Look up an FDIC institution by certificate number."""
        return self._http.get(f"/v1/financial/fdic/institution/{cert_number}")

    def search_brokers(self, name: Optional[str] = None, crd_number: Optional[str] = None, firm_name: Optional[str] = None, state: Optional[str] = None, limit: Optional[int] = None) -> dict:
        """Search FINRA-registered brokers."""
        body: dict[str, Any] = {}
        if name:
            body["name"] = name
        if crd_number:
            body["crdNumber"] = crd_number
        if firm_name:
            body["firmName"] = firm_name
        if state:
            body["state"] = state
        if limit is not None:
            body["limit"] = limit
        return self._http.post("/v1/financial/finra/brokers", body)

    def search_firms(self, name: Optional[str] = None, crd_number: Optional[str] = None, state: Optional[str] = None, limit: Optional[int] = None) -> dict:
        """Search FINRA-registered firms."""
        body: dict[str, Any] = {}
        if name:
            body["name"] = name
        if crd_number:
            body["crdNumber"] = crd_number
        if state:
            body["state"] = state
        if limit is not None:
            body["limit"] = limit
        return self._http.post("/v1/financial/finra/firms", body)
