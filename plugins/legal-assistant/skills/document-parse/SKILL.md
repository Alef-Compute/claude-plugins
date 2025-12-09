---
name: document-parse
description: Convert PDF or DOCX files to markdown. Use when you need to analyze a document's content. Preserves structure but not formatting.
---

# Document Parse

Convert documents to markdown for analysis.

## Usage
```bash
.claude/venv/bin/python .claude/skills/document-parse/scripts/convert.py <input_file> <output_file>
```

## Supported Formats
- PDF
- DOCX

## Output
Markdown file preserving:
- Headings and structure
- Tables
- Lists
- Paragraphs

Does NOT preserve: fonts, colors, images, tracked changes.

## Dependencies
Requires REDUCTO_API_KEY in environment. Dependencies installed via `.claude/requirements.txt`.
