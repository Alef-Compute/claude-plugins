# Playbook Schema

## How Playbooks Work

Playbooks OVERRIDE the foundational positions in `positions.md`:

- **positions.md** = Default positions for all clause types (balanced, market-standard)
- **playbook.md** = Custom positions that take precedence

**Include only clauses where you want DIFFERENT positions.**
Clauses not in playbook automatically use positions.md defaults.

## Playbook Structure

```markdown
---
name: "Acme Corp - SaaS Vendor Agreements"
type: client-specific  # or "general"
risk_tolerance: aggressive  # conservative, balanced, aggressive
last_updated: 2024-01-15
---

## liability_cap
**Position**: Cap at 6 months of fees (we push harder than market)
**Fallback**: Accept 12 months if vendor won't budge
**Walk-away**: Never accept unlimited liability
**Notes**: CFO approved this stance for deals under $100K

## indemnification
**Position**: Vendor indemnifies for IP, data breach, and negligence
**Fallback**: Accept mutual indemnification if capped at 24 months
**Walk-away**: Reject indemnification for our own negligence

# Clauses NOT listed here → use positions.md defaults
```

## Clause IDs

Use these IDs to override positions.md clauses:

| ID | Clause Type |
|----|-------------|
| liability_cap | Limitation of Liability |
| indemnification | Indemnification |
| termination | Termination Rights |
| payment_terms | Payment Terms |
| confidentiality | Confidentiality |
| intellectual_property | IP/Work Product |
| governing_law | Governing Law/Venue |
| data_protection | Data Protection/Privacy |
| insurance | Insurance Requirements |
| force_majeure | Force Majeure |
| assignment | Assignment/Change of Control |
| warranties | Warranties & Representations |
| dispute_resolution | Dispute Resolution |
| audit_rights | Audit Rights |
| mfn_clause | Most Favored Customer |

## Playbook Fields

| Field | Required | Description |
|-------|----------|-------------|
| Position | Yes | Preferred terms (overrides positions.md) |
| Fallback | No | Acceptable alternative if Position rejected |
| Walk-away | No | Absolute deal-breakers |
| Notes | No | Context for future reviews |

## Client Context Questions

When generating a new playbook, ask:

1. "What's your organization's general risk tolerance?" (Conservative/Balanced/Aggressive)
2. "Are there any specific clauses you always negotiate?"
3. "Any deal-breaker terms your organization never accepts?"
4. "What contract value range does this playbook cover?"
5. "Industry-specific concerns?" (Healthcare=HIPAA, Finance=audit rights, etc.)
