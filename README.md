# Inlead plugin

A plugin marketplace with one plugin, `inlead`, that connects AI assistants to
Inlead's MCP server and adds skills for conversion analysis and lead-capture
funnel building. One package serves Claude, ChatGPT, Codex and Cursor: the
skills and the MCP server are shared, and each platform reads its own
manifest.

> **Status: pre-release.** The plugin is functional but not yet listed in any
> public directory.

## What is inside

```
.claude-plugin/marketplace.json      # Claude marketplace
.agents/plugins/marketplace.json     # Codex marketplace
.cursor-plugin/marketplace.json      # Cursor marketplace
plugins/inlead/
├── .claude-plugin/plugin.json       # Claude manifest
├── .cursor-plugin/plugin.json       # Cursor manifest
├── plugin.json                      # portable manifest (Agent Plugins) with the OpenAI listing
├── .mcp.json                        # MCP server for Claude and Cursor (type http)
├── mcp.json                         # MCP server for ChatGPT and Codex (type streamable-http)
├── assets/logo.svg                  # square logo used by OpenAI and Cursor
├── README.md                        # listing description
└── skills/
    ├── setup/                       # connects the account, diagnoses sign-in errors
    ├── digest/                      # read-only portfolio digest
    ├── performance/                 # read-only drop-off diagnosis
    ├── lead-insights/               # read-only profile of the leads from their answers
    ├── review-funnel/               # read-only structural review
    ├── improve-funnel/              # applies review fixes after a rehearsal and confirmation
    ├── new-funnel/                  # drafts a funnel after confirmation (user-invoked)
    └── build-funnel/                # reference architecture + rules (model-invoked)
        └── examples/                # one worked example per funnel objective, loaded on demand
```

Both MCP files point at `https://api.ai.inlead.tech/mcp`. The user signs in
with OAuth; no file carries a token.

## Install

Users need an Inlead account with an active plan. There is no token to copy:
the client opens an Inlead page where the user signs in and approves the
access. Step-by-step guide for end users: [docs/installation.md](docs/installation.md).

| Client | How |
|---|---|
| claude.ai, Claude Desktop | **Customize** → **Plugins** → install **Inlead** (from the directory, or **Add marketplace** with `https://github.com/inlead-digital/inlead-plugin`), then **Connect** |
| Claude Code | `claude plugin marketplace add inlead-digital/inlead-plugin` → `claude plugin install inlead@inlead --scope user` → `/mcp` → **Authenticate** |
| ChatGPT | `chatgpt.com/plugins` → **Inlead** → connect (after the listing is approved) |
| Codex | `codex plugin marketplace add inlead-digital/inlead-plugin` → install **Inlead** from `/plugins` |
| Cursor | Install **Inlead** from the Cursor marketplace, then **Connect** in the MCP settings |

## Skills

| Skill | Invoked by | What it does |
|---|---|---|
| `inlead:setup` | user or model | Checks the connection and walks through signing in |
| `inlead:digest [period]` | user or model | Read-only portfolio digest: volume, leads, conversion, what moved |
| `inlead:performance [funnel]` | user or model | Read-only drop-off diagnosis; picks the worst funnel when none is given |
| `inlead:lead-insights [funnel] [period]` | user or model | Read-only profile of the leads from the distribution of their answers |
| `inlead:review-funnel [funnel]` | user or model | Read-only structural review of a draft |
| `inlead:improve-funnel [funnel]` | user or model | Applies the fixes of a review: proposes, rehearses without saving, confirms once, then edits |
| `inlead:new-funnel [briefing]` | user | Drafts a funnel; shows the structure and waits for confirmation before writing |
| `inlead:build-funnel` | model | Reference architecture and conversion best practices for quiz funnels |

In Claude Code the skills run as `/inlead:<skill>`. The read-only skills
remove the write tools from the model's reach while they run
(`disallowed-tools`); that field and `disable-model-invocation` are enforced by
Claude Code only. On other platforms the protection is the server's: the write
tools are annotated as write operations, and the connection only carries the
edit permission when the user left it checked.

## Content rule

Skills carry **routing** (which tool to use, in what order) and **domain
knowledge** (what makes a funnel convert), in provider-neutral language.

Operational protocol rules — batching, `document_hash`, write budget, omitted
fields — **do not live here**. They live in the `guide` the server returns from
`list_components`, versioned together with the backend. Duplicating them
creates a second source of truth that drifts silently.

## Publish

Keep `version` equal in the three plugin manifests and in
`.claude-plugin/marketplace.json`; raise it on every release. Then build the
upload packages:

```bash
python3 scripts/package.py
```

It checks that the versions match and writes to `dist/`. The CI
(`.github/workflows/validate.yml`) runs the validation and this script on every
pull request, and attaches the packages to each `v*` tag's release:

- `inlead-claude-<version>.zip` — Claude package, for claude.ai organization
  uploads.
- `inlead-openai-<version>.zip` — skills package for the OpenAI portal. It
  leaves out the MCP files: the server is registered by URL in the **With MCP**
  step.

| Platform | Where | What it reads |
|---|---|---|
| Claude directory | `claude.ai/directory/manage` — submit the plugin bundle (GitHub repository, folder `plugins/inlead`) and the MCP server as a connector | `.claude-plugin/plugin.json`, `.mcp.json`, `README.md`, `skills/` |
| OpenAI (ChatGPT + Codex) | `platform.openai.com/plugins` — **With MCP**: server URL, then the skills package | `plugin.json` (`extensions.com.openai`), `skills/`, `assets/` |
| Cursor | `cursor.com/marketplace/publish` (curated) or `cursor.directory` | `.cursor-plugin/plugin.json`, `.mcp.json`, `skills/`, `assets/` |

The Claude directory and Cursor read the plugin from a public GitHub
repository.

## Support and privacy

- Help center: https://ajuda.inlead.digital/
- Support: suporte@inlead.digital
- Privacy policy: https://inlead.digital/comunicados/politica-de-privacidade/
- Terms of use: https://inlead.digital/comunicados/termos-de-uso/
- Publisher: Inlead Digital Ltda. · CNPJ 55.751.771/0001-02 · São José do Rio Preto, SP, Brazil
- License: MIT (see [LICENSE](LICENSE))

The plugin sends requests only to Inlead's MCP server (`api.ai.inlead.tech`)
and only with the access the user approved on the Inlead sign-in page. It
reads funnel structure, aggregated analytics and aggregated answer
distributions; it never reads individual leads' contact data, nor the user's
files, chat history or memory.

## Development

Install from the local checkout as a marketplace. Plugins from a directory
marketplace are loaded **from source** on every session, so edits take effect
after a restart — no reinstall or version bump needed:

```bash
claude plugin marketplace add /path/to/this/repository
claude plugin install inlead@inlead --scope user
```

`claude --plugin-dir ./plugins/inlead` also loads the skills and the MCP server
for quick iteration; sign in once with `/mcp` → **Authenticate**.

Validate before committing (warnings become errors with `--strict`):

```bash
claude plugin validate . --strict
claude plugin validate ./plugins/inlead --strict
```

If the MCP server does not show up in `/mcp`, the `/plugin` Errors tab will
**not** tell you why. Run `claude --debug -p "ok"` and read
`~/.claude/debug/latest`: an invalid `.mcp.json` entry is logged as
`Invalid MCP server config`; an expired or revoked session as `UNAUTHENTICATED`.

To test against a non-production server, temporarily change the `url` in both
MCP files and restart the session. Do not commit that change: the published
plugin always points at production so that a user cannot be talked into
signing in to another server.
