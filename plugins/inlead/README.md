# Inlead

Connect your Inlead account to your AI assistant — Claude, ChatGPT, Codex or
Cursor — to understand how your lead-capture funnels and quizzes perform and to
build better ones. Ask for a digest of every funnel, find where people drop
off and why, see who your leads are from their answers, review a draft
against proven conversion practices for quiz funnels and apply the
fixes, or draft a new funnel from a briefing.

## What you can ask

- "Which of my funnels converts worst, and where do people drop off?"
- "Give me a digest of all my funnels for this month."
- "Who are the leads of my quiz, based on what they answer?"
- "Review my funnel draft before I publish it, then apply the fixes."
- "Draft a quiz funnel for a dental clinic that offers a free evaluation."

## Skills

| Skill | What it does |
|---|---|
| `inlead:setup` | Checks the connection and walks through signing in |
| `inlead:digest` | Read-only digest of every funnel for a period: volume, leads, conversion, what moved |
| `inlead:performance` | Read-only diagnosis of the step where a funnel loses the most people, and why |
| `inlead:lead-insights` | Read-only profile of a funnel's leads from the distribution of their answers |
| `inlead:review-funnel` | Read-only structural review of a draft, plus whether it is valid to publish |
| `inlead:improve-funnel` | Applies the fixes of a review or your list of changes: rehearses them without saving and waits for your confirmation |
| `inlead:new-funnel` | Drafts a funnel from a briefing; shows the plan and waits for your confirmation before saving |
| `inlead:build-funnel` | Reference architecture and conversion best practices for quiz funnels, used by the assistant when it builds or edits |

## Requirements

- An Inlead account with an active plan.
- The first time, your assistant opens an Inlead page where you sign in and
  approve the access. Reading your funnels is always included; creating and
  editing funnels can be turned off on that page. There is no token to copy.

## What the plugin connects to

- One remote MCP server, `https://api.ai.inlead.tech/mcp`, operated by Inlead.
  The plugin has no hooks, scripts, local executables or local servers.
- It reads funnel structure, aggregated metrics and aggregated answer
  distributions. It never reads individual leads' contact data, and never your
  files, chat history or memory.
- It writes only to funnel drafts, only after you confirm, and never publishes:
  you review and publish in the Inlead editor.
- Each sign-in is a separate connection that you can see and disconnect in the
  Inlead dashboard under "Minha conta > Integrações".

## Support and privacy

- Help center: https://ajuda.inlead.digital/
- Support and security reports: suporte@inlead.digital
- Privacy policy: https://inlead.digital/comunicados/politica-de-privacidade/
- Terms of use: https://inlead.digital/comunicados/termos-de-uso/
- Publisher: Inlead Digital Ltda. · CNPJ 55.751.771/0001-02 · São José do Rio Preto, SP, Brazil
- License: MIT
