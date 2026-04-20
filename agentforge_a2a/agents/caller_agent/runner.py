"""Deterministic runner for caller-agent. Pure function, no side effects."""

from __future__ import annotations


class CallerRunner:
    def run(self, input_text: str) -> str:
        return f"called->{input_text}"
