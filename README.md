# agentforge-a2a-plugin

Test rig for AgentForge's agent-to-agent dispatch. Canonical smoke for `POST /invoke/{ns}/{group}/{name}` and the depth + circular-delegation guards layered on top of it. Filed as [TAP-758](https://linear.app/tappscodingagents/issue/TAP-758) under the Plugin System Coverage Wave A epic ([TAP-755](https://linear.app/tappscodingagents/issue/TAP-755)).

## What it proves works

| Hook | How |
|------|-----|
| Namespace resolution | Two agents at `project.a2a.caller-agent` and `project.a2a.callee-agent` resolve via `/invoke/project.a2a/group/{name}` |
| Depth guard | Chain ≥ 3 → HTTP 429 with `{error: "invoke_depth_exceeded", chain}` |
| Circular delegation detection | Target already in chain → HTTP 409 with `{error: "circular_delegation", cycle}` |
| 404 on unresolved agent | Unknown namespace → HTTP 404 |
| `load_external()` namespace-prefix enforcement | Agents under `project.a2a.*` only |

## Install

```bash
uv pip install -e /path/to/agentforge-a2a-plugin
```

Against a running AgentForge:

```bash
curl -XPOST http://127.0.0.1:8001/api/plugins/register \
  -H 'content-type: application/json' \
  -d '{"package_name":"agentforge_a2a"}'

curl -XPOST http://127.0.0.1:8001/invoke/project.a2a/group/callee-agent \
  -H 'content-type: application/json' \
  -d '{"prompt":"hello"}'
```

## Run plugin-side tests

```bash
cd /path/to/agentforge-a2a-plugin
uv run --with pytest pytest
```

## What this rig is **not** testing

- Full agent execution end-to-end (orchestrator, brain, memory) — that's an integration test.
- Policy guards (`RiskLevelGuard`, `BudgetGuard`) — see the policy-plugin rig ([TAP-761](https://linear.app/tappscodingagents/issue/TAP-761)).

The caller-agent does not programmatically invoke callee-agent at runtime; both exist only so `/invoke` can resolve them. The **dispatch surface** is what's under test, not agent-level delegation logic.

## Pattern

Follows the echo plugin's canonical pattern ([TAP-753](https://linear.app/tappscodingagents/issue/TAP-753)). See [docs/PLUGIN_RIGS.md](https://github.com/wtthornton/AgentForge/blob/main/docs/PLUGIN_RIGS.md) in the AgentForge repo for the rig index + how-to-build.
