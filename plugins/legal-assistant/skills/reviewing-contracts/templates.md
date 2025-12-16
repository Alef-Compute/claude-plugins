# Issue Presentation Templates

## Interactive Mode - Single Issue

```
## Issue [N] - [SEVERITY]: [Title]

**Section**: [number]
**Current**: "[exact quote]"
**Risk**: [one sentence]
**Position**: [playbook/default says]
**Source**: [playbook or positions.md]
**Revision**: "[proposed]"

Approve? (yes/no/modify)
```

## Autonomous Mode - Summary

```
## Review Summary

| # | Section | Severity | Issue | Resolution |
|---|---------|----------|-------|------------|

### Unchanged (met standards)
- [list]

**Stats:**
- Issues found: X
- Revisions applied: Y
- Items for senior counsel: Z
```

## Pre-Delivery Quality Checklist

Before generating redlined document:

- [ ] All HIGH severity issues addressed or explicitly acknowledged by user
- [ ] Revision language is grammatically correct and reads naturally
- [ ] Changes maintain document flow (no dangling references)
- [ ] Defined terms used consistently (capitalization matches original)
- [ ] No orphaned cross-references to deleted sections
- [ ] Playbook fallback positions used where primary was rejected
- [ ] Diff verified: only intended changes present

## Concrete Example

**Issue 2 - HIGH: Unlimited Liability**

**Section**: 8.1 Limitation of Liability
**Current**: "IN NO EVENT SHALL EITHER PARTY'S LIABILITY EXCEED THE AMOUNTS PAID HEREUNDER, EXCEPT FOR BREACHES OF CONFIDENTIALITY, INDEMNIFICATION OBLIGATIONS, OR GROSS NEGLIGENCE, FOR WHICH LIABILITY SHALL BE UNLIMITED."
**Risk**: Unlimited liability for confidentiality breaches exposes us to uncapped damages
**Position**: Liability capped at 12 months of fees for all claims
**Source**: positions.md (default)
**Revision**: "IN NO EVENT SHALL EITHER PARTY'S LIABILITY EXCEED TWELVE (12) MONTHS OF FEES PAID OR PAYABLE HEREUNDER."

Approve? (yes/no/modify)
