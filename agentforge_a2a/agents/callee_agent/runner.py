"""Deterministic runner for callee-agent. Pure function, no side effects."""

from __future__ import annotations


class CalleeRunner:
    def run(self, input_text: str) -> str:
        return input_text.upper()
