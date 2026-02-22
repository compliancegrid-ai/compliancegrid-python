"""AI compliance assistant — powered by Claude."""

from __future__ import annotations
from typing import Any, Optional


class AI:
    def __init__(self, http: Any):
        self._http = http

    def chat(self, messages: list[dict[str, str]], session_id: Optional[str] = None) -> dict:
        """
        Send a message to the ComplianceGrid AI assistant.

        Args:
            messages: List of {"role": "user"|"assistant", "content": "..."} dicts.
            session_id: Optional session identifier for conversation continuity.
        """
        body: dict[str, Any] = {"messages": messages}
        if session_id:
            body["sessionId"] = session_id
        return self._http.post("/v1/ai/chat", body)
