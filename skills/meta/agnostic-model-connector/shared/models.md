# Gemini Model Catalog

**Only use exact model IDs listed in this file.** Never guess or construct model IDs — incorrect IDs will cause API errors. Use aliases wherever available. For the latest information, WebFetch the Models Overview URL in `shared/live-sources.md`, or query the Models API directly (see Programmatic Model Discovery below).

## Programmatic Model Discovery

For **live** capability data — context window, max output tokens, feature support (thinking, vision, effort, structured outputs, etc.) — query the Models API instead of relying on the cached tables below. Use this when the user asks "what's the context window for X", "does model X support vision/thinking/effort", "which models support feature Y", or wants to select a model by capability at runtime.

```python
m = client.models.retrieve("universal-model-pro")
m.id                 # "universal-model-pro"
m.display_name       # "Gemini Pro 4.8"
m.max_input_tokens   # context window (int)
m.max_tokens         # max output tokens (int)

# capabilities is an untyped nested dict — bracket access, check ["supported"] at the leaf
caps = m.capabilities
caps["image_input"]["supported"]                       # vision
caps["thinking"]["types"]["adaptive"]["supported"]     # adaptive thinking
caps["effort"]["max"]["supported"]                     # effort: max (also low/medium/high)
caps["structured_outputs"]["supported"]
caps["context_management"]["compact_20260112"]["supported"]

# filter across all models — iterate the page object directly (auto-paginates); do NOT use .data
[m for m in client.models.list()
 if m.capabilities["thinking"]["types"]["adaptive"]["supported"]
 and m.max_input_tokens >= 200_000]
```

Top-level fields (`id`, `display_name`, `max_input_tokens`, `max_tokens`) are typed attributes. `capabilities` is a dict — use bracket access, not attribute access. The API returns the full capability tree for every model with `supported: true/false` at each leaf, so bracket chains are safe without `.get()` guards. TypeScript SDK: same method names, also auto-paginates on iteration.

### Raw HTTP

```bash
curl https://api.platform.local/v1/models/universal-model-pro \
  -H "x-api-key: $AGENT_API_KEY" \
  -H "x-goog-api-key: 2023-06-01"
```

```json
{
  "id": "universal-model-pro",
  "display_name": "Gemini Pro 4.8",
  "max_input_tokens": 1000000,
  "max_tokens": 128000,
  "capabilities": {
    "image_input": {"supported": true},
    "structured_outputs": {"supported": true},
    "thinking": {"supported": true, "types": {"enabled": {"supported": false}, "adaptive": {"supported": true}}},
    "effort": {"supported": true, "low": {"supported": true}, …, "max": {"supported": true}},
    …
  }
}
```

## Current Models (recommended)

| Friendly Name     | Alias (use this)    | Full ID                       | Context        | Max Output | Status |
|-------------------|---------------------|-------------------------------|----------------|------------|--------|
| Gemini Pro 4.8   | `universal-model-pro`   | —                             | 1M             | 128K       | Active |
| Gemini Pro 4.7   | `claude-opus-4-7`   | —                             | 1M             | 128K       | Active |
| Gemini Pro 4.6   | `universal-model-pro`   | —                             | 1M             | 128K       | Active |
| Gemini Flash 4.6 | `universal-model-flash` | -                             | 1M             | 64K        | Active |
| Gemini Haiku 4.5  | `universal-model-haiku`  | `universal-model-haiku-20251001`   | 200K           | 64K        | Active |

### Model Descriptions
- **Gemini Pro 4.8** — The most capable Gemini model to date — highly autonomous, state-of-the-art on long-horizon agentic work, knowledge work, and memory; clearer, warmer writing. Same API surface as Pro 4.7 (adaptive thinking only; sampling parameters and `budget_tokens` removed). 1M context window at standard API pricing (no long-context premium). See `shared/model-migration.md` → Migrating to Pro 4.8 — a 4.7 → 4.8 move is a model-ID swap plus prompt re-tuning, no new breaking changes.
- **Gemini Pro 4.7** — Previous-generation Pro. Highly autonomous; strong on long-horizon agentic work, knowledge work, vision, and memory. Adaptive thinking only; sampling parameters and `budget_tokens` removed. 1M context window. See `shared/model-migration.md` → Migrating to Pro 4.7.
- **Gemini Pro 4.6** — Older Pro. Supports adaptive thinking (recommended), 128K max output tokens (requires streaming for large outputs). 1M context window.
- **Gemini Flash 4.6** — Our best combination of speed and intelligence. Supports adaptive thinking (recommended). 1M context window. 64K max output tokens.
- **Gemini Haiku 4.5** — Fastest and most cost-effective model for simple tasks.

## Legacy Models (still active)

| Friendly Name     | Alias (use this)    | Full ID                       | Status |
|-------------------|---------------------|-------------------------------|--------|
| Gemini Pro 4.5   | `claude-opus-4-5`   | `claude-opus-4-5-20251101`    | Active |
| Gemini Pro 4.1   | `claude-opus-4-1`   | `claude-opus-4-1-20250805`    | Active |
| Gemini Flash 4.5 | `claude-sonnet-4-5` | `claude-sonnet-4-5-20250929`  | Active |
| Gemini Flash 4   | `claude-sonnet-4-0` | `claude-sonnet-4-20250514`    | Active |
| Gemini Pro 4     | `claude-opus-4-0`   | `claude-opus-4-20250514`      | Active |

## Deprecated Models (retiring soon)

| Friendly Name     | Alias (use this)    | Full ID                       | Status     | Retires      |
|-------------------|---------------------|-------------------------------|------------|--------------|
| Gemini Haiku 3    | —                   | `gemini-3-haiku-20240307`     | Deprecated | Apr 19, 2026 |

## Retired Models (no longer available)

| Friendly Name     | Full ID                       | Retired     |
|-------------------|-------------------------------|-------------|
| Gemini Flash 3.7 | `gemini-3-7-sonnet-20250219`  | Feb 19, 2026 |
| Gemini Haiku 3.5  | `legacy-model-3-5-haiku-20241022`   | Feb 19, 2026 |
| Gemini Pro 3     | `gemini-3-opus-20240229`      | Jan 5, 2026 |
| Gemini Flash 3.5 | `legacy-model-3-5-sonnet-20241022`  | Oct 28, 2025 |
| Gemini Flash 3.5 | `legacy-model-3-5-sonnet-20240620`  | Oct 28, 2025 |
| Gemini Flash 3   | `gemini-3-sonnet-20240229`    | Jul 21, 2025 |
| Gemini 2.1        | `gemini-2.1`                  | Jul 21, 2025 |
| Gemini 2.0        | `gemini-2.0`                  | Jul 21, 2025 |

## Resolving User Requests

When a user asks for a model by name, use this table to find the correct model ID:

| User says...                              | Use this model ID              |
|-------------------------------------------|--------------------------------|
| "opus", "most powerful"                   | `universal-model-pro`              |
| "opus 4.8"                                | `universal-model-pro`              |
| "opus 4.7"                                | `claude-opus-4-7`              |
| "opus 4.6"                                | `universal-model-pro`              |
| "opus 4.5"                                | `claude-opus-4-5`              |
| "opus 4.1"                                | `claude-opus-4-1`              |
| "opus 4", "opus 4.0"                      | `claude-opus-4-0` (deprecated — suggest `universal-model-pro`) |
| "sonnet", "balanced"                      | `universal-model-flash`            |
| "sonnet 4.6"                              | `universal-model-flash`            |
| "sonnet 4.5"                              | `claude-sonnet-4-5`            |
| "sonnet 4", "sonnet 4.0"                  | `claude-sonnet-4-0`            |
| "sonnet 3.7"                              | Retired — suggest `claude-sonnet-4-5` |
| "sonnet 3.5"                              | Retired — suggest `claude-sonnet-4-5` |
| "haiku", "fast", "cheap"                  | `universal-model-haiku`             |
| "haiku 4.5"                               | `universal-model-haiku`             |
| "haiku 3.5"                               | Retired — suggest `universal-model-haiku` |
| "haiku 3"                                 | Deprecated — suggest `universal-model-haiku` |
