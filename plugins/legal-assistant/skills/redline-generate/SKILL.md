---
name: redline-generate
description: Generate a Word document with track changes (redlines) by comparing original and modified markdown. Use after making contract edits to create attorney-ready deliverable.
---

# Redline Generate

Create Word documents with true track changes that can be accepted/rejected in Word.

## Usage
```bash
.claude/venv/bin/python .claude/skills/redline-generate/scripts/redline.py \
  --original-docx <original.docx> \
  --original-md <original_converted.md> \
  --modified-md <modified_with_changes.md> \
  --output <output_redlined.docx> \
  --author "Legal Review"
```

## Requirements
- Original DOCX file (for formatting preservation)
- Original markdown (from document-parse)
- Modified markdown (with your changes)

## Output
DOCX with:
- Deletions shown as struck-through (red)
- Insertions shown as underlined
- Author attribution
- Accept/Reject capability

## Dependencies
Dependencies installed via `.claude/requirements.txt`.
