---
name: callee-agent
namespace: project.a2a.callee-agent
description: Downstream-side marker agent for AgentForge A2A dispatch smoke. Deterministic runner uppercases input; exists so /invoke/project.a2a/group/callee-agent resolves to a real AgentConfig.
keywords: [a2a, dispatch, test, callee]
utterances:
  - receive delegation
  - test a2a callee
model: sonnet
memory_profile: none
runner: agentforge_a2a.agents.callee_agent.runner:CalleeRunner
---

# Callee Agent

Downstream marker for A2A dispatch tests. Deterministic uppercase transform.
