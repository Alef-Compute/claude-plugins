---
name: reviewing-contracts
description: Reviews commercial contracts against playbook positions and generates redlined Word documents. Triggers when reviewing contracts, redlining agreements, analyzing terms, marking up NDAs/MSAs/SOWs/SaaS agreements, checking for risky clauses, comparing against playbooks, or building contract playbooks.
---

# Contract Review

Reviews contracts against playbook positions and generates redlined deliverables.

## Checklist

```
- [ ] 1. Playbook discovery/management
- [ ] 2. Convert document and analyze
- [ ] 3. Get review mode preference
- [ ] 4. Present issues, collect approvals, create Approved Changes Document
- [ ] 5. Generate redlined DOCX
- [ ] 6. Report completion
```

---

## Workspace Directory

**All generated files MUST be placed in `.claude/workspace/`** in the working directory.

This includes:
- Converted documents (e.g., `contract_analysis.md`)
- Approved changes documents
- Python scripts for redlining
- Unpacked document directories
- Final redlined documents

The `$WORKSPACE_DIR` environment variable is automatically set to this path.

**Examples:**
- `$WORKSPACE_DIR/contract_analysis.md`
- `$WORKSPACE_DIR/approved_changes.md`
- `$WORKSPACE_DIR/unpacked/` (for docx unpacking)
- `$WORKSPACE_DIR/scripts/batch1.py`
- `$WORKSPACE_DIR/output/contract_redlined.docx`

**Never** create files in:
- The user's project root directory
- `/tmp/` or other system directories
- The plugin directory itself

---

## Step 1: Playbook Discovery & Management

1. **Search for existing playbook:**
   - Look in `playbooks/` directory inside `$CLAUDE_PROJECT_DIR`
   - Check for client-specific: `playbooks/<client_name>.md`
   - Check for general: `playbooks/default.md`

2. **If playbook found:** Confirm with user before using

3. **If no playbook found:**
   - Ask user if one exists elsewhere
   - If none exists, offer to generate one interactively

4. **Playbook generation (if needed):**
   - Ask: contract type, risk tolerance, specific concerns, client vs general use
   - Generate from [positions.md](positions.md) defaults
   - Present draft for user review and tweaking
   - Save to `playbooks/` for reuse

5. **Position resolution during analysis:**
   - Playbook position → USE IT
   - Not in playbook → USE positions.md default
   - Log which source was used

See [references/playbook-schema.md](references/playbook-schema.md) for playbook format.

## Step 2: Convert Document and Analyze

Convert to markdown using pandoc (output to workspace):

```bash
pandoc --track-changes=all <contract.docx> -o "$WORKSPACE_DIR/contract_analysis.md"
```

Then analyze each clause against playbook/positions.md. See [positions.md](positions.md) for:
- 15 clause types with clause IDs
- Red flags and severity ratings
- Default positions and sample language

Rate deviations: **HIGH** (deal-breaker), **MEDIUM** (negotiate), **LOW** (flag).

## Step 3: Get Review Mode

Ask: "How would you like to review the findings?"

- **Interactive**: Best for high-stakes contracts, first reviews, complex agreements
- **Autonomous**: Best for routine reviews, time-sensitive, established playbooks

## Step 4: Present Issues and Collect Approvals

- **Interactive**: Present one issue at a time using [templates.md](templates.md), wait for approval
- **Autonomous**: Present all issues in summary table, get bulk approval

### Create Approved Changes Document

After all approvals collected, create a structured changes document that aligns with Anthropic's docx skill expected format:

```markdown
## Approved Changes for Redlining

### Batch 1: [Section/Type Description]
(Group 3-10 related changes per batch)

#### Change 1
- **Location Method**: Section 3.2, paragraph 1
- **Grep Pattern**: `unique surrounding text to find`
- **Delete**: "exact text to delete"
- **Insert**: "replacement text"

#### Change 2
- **Location Method**: Article IV, first paragraph
- **Grep Pattern**: `liability shall be unlimited`
- **Delete**: "liability shall be unlimited"
- **Insert**: "liability shall not exceed twelve (12) months of fees"

### Batch 2: [Section/Type Description]
...

## Summary
- Total batches: X
- Total changes: Y
```

**Location Method Guidelines** (per docx skill):
- Section/heading numbers: "Section 3.2", "Article IV"
- Paragraph identifiers: "first paragraph", "paragraph 3"
- Grep patterns: unique surrounding text to find in XML
- Document structure: "signature block", "definitions section"
- **DO NOT use markdown line numbers** - they don't map to XML

**Batching Guidelines** (per docx skill):
- Group 3-10 related changes per batch
- By section: "Batch 1: Section 2 amendments"
- By type: "Batch 1: Date corrections"
- By complexity: Simple replacements first, then structural changes

This document is consumed by Step 5 and formatted to match docx skill's workflow.

---

## Step 5: Generate Redlined DOCX

**Prerequisites:** Approved Changes Document from Step 4

### Use Anthropic's Docx Skill

Use Anthropic's `document-skills:docx` skill for redline generation.

1. **Read the docx skill's documentation** - Read SKILL.md and ooxml.md from the docx skill (path available in `$DOCX_SKILL`).

2. **Follow the "Tracked changes workflow"** exactly, step by step. Do not skip steps or deviate.

### Environment Notes

The following are automatically configured at session start:
- `$CLAUDE_PLUGIN_ROOT` - This plugin's directory
- `$DOCX_SKILL` - Anthropic's docx skill directory
- `$WORKSPACE_DIR` - Directory for all generated files (`.claude/workspace/`)
- Python 3.10 venv is auto-activated

### File Locations

All generated files go in `$WORKSPACE_DIR`:
- `$WORKSPACE_DIR/unpacked/` - Unpacked docx contents
- `$WORKSPACE_DIR/scripts/` - Python scripts for modifications
- `$WORKSPACE_DIR/output/` - Final redlined documents

### Critical Notes

**Always Use Absolute Paths:** The Document class requires absolute paths. Use the expanded `$WORKSPACE_DIR`:
```python
import os
doc = Document(f"{os.environ['WORKSPACE_DIR']}/unpacked", ...)
```

**Line Numbers Change:** After each batch of modifications, re-grep `document.xml` to get current line numbers.

---

## Step 6: Report

Provide:
- Deliverable location
- Changes summary (applied/total)
- Items flagged for senior counsel (any HIGH severity items not addressed)
- Option to update playbook with learnings
