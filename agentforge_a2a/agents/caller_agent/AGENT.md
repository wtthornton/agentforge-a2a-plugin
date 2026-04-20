---
name: caller-agent
namespace: project.a2a.caller-agent
description: Upstream-side marker agent for AgentForge A2A dispatch smoke. Deterministic transform prefixes input with "called->"; no LLM, no delegation logic of its own. Exists so /invoke/project.a2a/group/caller-agent resolves to a real AgentConfig.
keywords: [a2a, dispatch, test, caller]
utterances:
  - delegate to callee
  - test a2a caller
model: sonnet
memory_profile: none
runner: agentforge_a2a.agents.caller_agent.runner:CallerRunner
---

# Caller Agent

Upstream marker for A2A dispatch tests. Runner is a pure function; the test rig is not about delegation *logic* but about the dispatch *infrastructure* (depth guard, cycle detection, namespace resolution).
