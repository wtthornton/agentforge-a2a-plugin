"""AgentForge plugin entry point for agentforge-a2a-plugin.

Contributes two agents under `project.a2a`:
- caller-agent  → marker runner for the upstream side of an A2A chain
- callee-agent  → marker runner for the downstream side

The plugin itself mounts no HTTP routes. The A2A dispatch surface being
tested is AgentForge's own `POST /invoke/{ns}/{group}/{name}`.
"""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI

logger = logging.getLogger(__name__)

_AGENTS_DIR = Path(__file__).parent / "agents"
_NAMESPACE = "project.a2a"


def register(app: FastAPI) -> None:
    agent_loader = getattr(app.state, "agent_loader", None)
    if agent_loader is None:
        logger.debug("a2a plugin: no agent_loader on app.state — skipping agent load")
        return

    try:
        newly_loaded = agent_loader.load_external(_AGENTS_DIR, _NAMESPACE)
        logger.info("a2a plugin: loaded %d agent(s)", len(newly_loaded))
    except Exception:
        logger.exception("a2a plugin: agent load failed")
