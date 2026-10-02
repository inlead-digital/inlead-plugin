# Security

To report a vulnerability in this plugin or in Inlead's MCP server, e-mail
**suporte@inlead.digital** with "security" in the subject. Please do not open
a public issue for security reports.

## What this plugin touches

- Sends requests only to `https://api.ai.inlead.tech/mcp`, with the access the
  user approved on the Inlead sign-in page (OAuth 2.1 with PKCE). The session is
  kept in the client's secure storage; no password or token is typed into the
  assistant, on any platform.
- The access is read-only or read and write, as chosen on the sign-in page.
  Each connection can be revoked in the Inlead dashboard under
  "Minha conta > Integrações" and stops working immediately.
- Reads funnel structure, aggregated metrics and aggregated answer
  distributions; never individual leads' contact data.
- No hooks, no sub-agents, no scripts, no local executables, no local MCP
  servers.
