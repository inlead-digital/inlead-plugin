# Installing the Inlead plugin

You only need an Inlead account with an active plan. There is no token to
copy: your assistant opens an Inlead page where you sign in and approve the
access. Reading your funnels is always included; you can uncheck **editing**
on that page to connect in read-only mode.

## Claude (claude.ai web or Claude Desktop)

1. Left sidebar → **Customize** → **Plugins**. Install **Inlead** from the
   directory, or add the Inlead marketplace: **Personal plugins** → **"+"** →
   **Add marketplace** → **Add from a repository** → paste the marketplace URL.
   *If your organization already provides the plugin, it is listed there.*
2. Click **Install** on **Inlead**. The connector dialog opens, already filled
   with Inlead's server: keep the defaults, add no header, and confirm.
3. Click **Connect** on the Inlead connector. The Inlead page opens: sign in if
   asked, review the access and click **Permitir** (*Allow*).
4. Open a new chat and type `/inlead:setup` to confirm.

> Do **not** add Inlead as a custom connector by URL: you would get the server
> without the plugin's skills.

## Claude Code (terminal or VS Code)

```bash
claude plugin marketplace add inlead-digital/inlead-plugin
claude plugin install inlead@inlead --scope user
```

Then type `/mcp`, pick the Inlead server and choose **Authenticate**. The
browser opens the same Inlead page: sign in if asked and click **Permitir**.

## ChatGPT

1. Open **Plugins** (`chatgpt.com/plugins`), find **Inlead** and connect it.
2. The Inlead page opens: sign in if asked and click **Permitir**.
3. In a new chat, ask for what you need; if ChatGPT does not use Inlead,
   select it from the **+** menu.

## Codex

```bash
codex plugin marketplace add inlead-digital/inlead-plugin
```

Then open `/plugins`, install **Inlead** and sign in on the Inlead page when
Codex asks.

## Cursor

1. Install **Inlead** from the Cursor marketplace.
2. In Cursor's MCP settings, click **Connect** next to Inlead. The browser
   opens the Inlead page: sign in if asked and click **Permitir**.

## Use

Ask in your own words, for example:

- *"Which of my funnels converts worst, and where do people drop off?"*
- *"Give me a digest of all my funnels for this month."*
- *"Who are the leads of my quiz, based on what they answer?"*
- *"Review my funnel draft before I publish it, then apply the fixes."*
- *"Draft a quiz funnel for a dental clinic that offers a free evaluation."*

| Skill | What it does |
|---|---|
| `inlead:setup` | Checks the connection and explains how to sign in |
| `inlead:digest` | Summary of all funnels for a period |
| `inlead:performance [funnel]` | Where people drop off, and why |
| `inlead:lead-insights [funnel]` | Who your leads are, from their answers |
| `inlead:review-funnel [funnel]` | Structural review of a draft |
| `inlead:improve-funnel [funnel]` | Applies the review's fixes (asks for confirmation before saving) |
| `inlead:new-funnel [briefing]` | Drafts a funnel (asks for confirmation before writing) |

In Claude Code, run them as `/inlead:<skill>`.

## Manage the connection

Every sign-in is its own connection: connecting another app or computer does
not disconnect the first. See and disconnect them in the Inlead dashboard
under **"Minha conta > Integrações"** (My account > Integrations): Claude in
the Claude section, ChatGPT in the OpenAI section, other apps under **"Outros
aplicativos"** in the MCP section. A connection keeps working while you use
it; after 30 days without use, or 90 days in total, sign in again.

## Common problems

| Symptom | Likely cause | What to do |
|---|---|---|
| `UNAUTHENTICATED` | The connection expired or was disconnected, or an old token is still set as a header | Sign in again; if you had configured a token header (plugin 0.4.x or by hand), remove it |
| `ABILITY_REQUIRED` when editing | You connected in read-only mode | Disconnect in the dashboard and sign in again keeping **editing** checked |
| `SUBSCRIPTION_REQUIRED` | The account has no active plan, or the plan does not include that feature | Check the plan in the Inlead dashboard |
| Inlead tools do not appear | The plugin was not installed, or you have not signed in yet | Reinstall the plugin and sign in |
| The Inlead page says the subscription is inactive | The account has no active plan | Regularize the plan, then connect again |
| The Inlead page says the limit of connected apps was reached | 20 active connections | Disconnect an old one in "Minha conta > Integrações" |
| `ACCOUNT_BLOCKED` | Account blocked on the platform | Contact support |

Support: suporte@inlead.digital · Help center: https://ajuda.inlead.digital
