---
name: contract-review
description: Reviews commercial contracts against playbook positions, generates redlined Word documents. Use when user asks to review, redline, analyze, or mark up a contract, NDA, MSA, or agreement.
---

# Contract Review

Reviews contracts against playbook positions and generates redlined deliverables.

## Checklist

Copy and track progress:

```
- [ ] 0. Verify dependencies
- [ ] 1. Gather context (file, playbook, client)
- [ ] 2. Convert document to markdown
- [ ] 3. Analyze against positions
- [ ] 4. Get review mode preference
- [ ] 5. Present/apply changes
- [ ] 6. Generate redlined DOCX
- [ ] 7. Verify deliverable quality
- [ ] 8. Report completion
```

## Step 0: Verify Dependencies

Set up isolated environment (does not modify user's system Python):

```bash
# Create venv if missing
[ ! -d ".claude/venv" ] && python3 -m venv .claude/venv

# Install dependencies (quiet mode, only shows errors)
.claude/venv/bin/pip install -q -r .claude/requirements.txt

# Verify installation
.claude/venv/bin/python -c "import requests; from docx import Document; from lxml import etree; print('Environment OK')"
```

Check API key (needed for document conversion):
```bash
[ -z "$REDUCTO_API_KEY" ] && echo "⚠️ REDUCTO_API_KEY not set - ask user for API key"
```

If REDUCTO_API_KEY is missing, ask user to provide it before proceeding.

## Step 1: Gather Context

1. Identify contract file (PDF/DOCX)
2. Search `playbooks/` for applicable playbook
3. Infer client from folder structure
4. **If no playbook**: Ask user for positions (see `positions.md`)

## Step 2: Convert Document

```bash
.claude/venv/bin/python .claude/skills/document-parse/scripts/convert.py <input> .claude/workspace/working/<name>_work.md
cp .claude/workspace/working/<name>_work.md .claude/workspace/working/<name>_work_copy.md
```

## Step 3: Analyze

Compare each clause against playbook. See `positions.md` for clause types and red flags.

Rate deviations: HIGH (deal-breaker), MEDIUM (negotiate), LOW (minor).

## Step 4: Get Mode

Ask: "Interactive (approve each) or autonomous (apply all, show summary)?"

## Step 5: Present/Apply

- **Interactive**: Present one issue at a time, wait for approval. See `templates.md`.
- **Autonomous**: Apply all, show summary table.

Edit the `_work_copy.md` file only.

## Step 6: Generate Deliverable

```bash
.claude/venv/bin/python .claude/skills/redline-generate/scripts/redline.py \
  --original-docx <original.docx> \
  --original-md .claude/workspace/working/<name>_work.md \
  --modified-md .claude/workspace/working/<name>_work_copy.md \
  --output .claude/workspace/output/<name>_redlined.docx
```

## Step 7: Verify Deliverable Quality

Feedback loop - verify before reporting:

1. Confirm output file exists and size > 0
2. Check track changes are visible: `.claude/venv/bin/python .claude/skills/redline-generate/scripts/redline.py --check-deps`
3. If changes not applied correctly, check:
   - Original DOCX matches the markdown source
   - Text being searched exists in document (case sensitivity)
   - Retry with more specific text matches

Ask user: "Would you like me to verify the redlined document looks correct before we finish?"

## Step 8: Report

- Deliverable location
- Changes summary (applied/total)
- Items for senior counsel (if any)
- Any warnings from redline generation
