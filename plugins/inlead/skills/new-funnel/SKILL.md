---
name: new-funnel
description: Draft a lead-capture funnel on Inlead from a briefing. Use only when the user explicitly asks to draft or create a new funnel. Writes to the account after explicit confirmation.
argument-hint: "[briefing]"
disable-model-invocation: true
compatibility: Requires a connection to Inlead's MCP server (sign in with the Inlead account; see the inlead:setup skill).
allowed-tools: mcp__plugin_inlead_inlead__list_funnels mcp__plugin_inlead_inlead__get_funnel_steps mcp__plugin_inlead_inlead__list_components mcp__plugin_inlead_inlead__get_component_contracts mcp__plugin_inlead_inlead__validate_funnel_draft
---

Draft a funnel on Inlead. Follow the `inlead:build-funnel` skill throughout.

The briefing is what the user wrote with the request.

## 1. Understand

If the briefing is empty or does not say enough, ask before building — at
minimum: what the business is, who the audience is, and what the funnel needs
to find out about the person. Do not invent those three. Then state the
objective you inferred: lead generation or direct sale.

## 2. Read a reference

`list_funnels`, then `get_funnel_steps` (structure only) on the account's
published funnel closest to the goal: its size, where it asks for contact,
which blocks it has. If there is none, say so and use the reference
architecture from `inlead:build-funnel`. Then `list_components` for the rules and
catalog, and the contracts of every type you will emit.

## 3. Propose in blocks, then in steps

First show the block plan with a step count per block, for example:

> Hook (1) → Segmentation (2) → Profiling + proof (5) → Loading (1) →
> Diagnosis (1) → Capture (1) → Offer / result (1) — 12 steps

Say which blocks of the reference architecture you left out and why. Then
detail each step: what it asks or shows, and where the contact request goes.
Validate with `validate_funnel_draft` before showing the final plan.

**Stop here and wait for the user's confirmation.** Do not write before it.

## 4. After confirmation

Persist as the server guide instructs (skeleton and batches for large
funnels). When done, say explicitly that the funnel was saved as a draft and
that the user needs to open the Inlead editor to review it before publishing
or sharing any link. List anything you left as a placeholder.
