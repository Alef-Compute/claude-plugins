# Redlining Guide

The redline generator finds exact text from the original markdown in the DOCX and applies track changes.

**Messy edits = broken redlines.** Follow these rules for clean output.

## The Workflow

1. **Convert original to markdown** (parsing-documents skill)
   ```bash
   .claude/venv/bin/python .claude/skills/parsing-documents/scripts/convert.py \
     original_contract.docx \
     .claude/workspace/working/contract_work.md
   ```

2. **Create a working copy**
   ```bash
   cp .claude/workspace/working/contract_work.md \
      .claude/workspace/working/contract_work_copy.md
   ```

3. **Edit ONLY the copy** - Never touch contract_work.md after this

4. **Generate redlines**
   ```bash
   .claude/venv/bin/python .claude/skills/generating-redlines/scripts/redline.py \
     --original-docx original_contract.docx \
     --original-md .claude/workspace/working/contract_work.md \
     --modified-md .claude/workspace/working/contract_work_copy.md \
     --output .claude/workspace/output/contract_redlined.docx
   ```

## Rules for Clean Edits

**DO:**
- Replace only the specific clause text that needs changing
- Match the exact text from the original (including capitalization)
- Keep surrounding text unchanged
- Make surgical, precise edits

**DON'T:**
- Reformat or re-wrap paragraphs
- Change whitespace or line breaks unnecessarily
- Edit surrounding text that doesn't need to change
- Add markdown formatting (headers, bullets) to existing text
- Fix typos or grammar in unrelated sections

## Example: Correct vs Incorrect

**Original text in markdown:**
```
IN NO EVENT SHALL EITHER PARTY'S LIABILITY EXCEED THE AMOUNTS PAID HEREUNDER, EXCEPT FOR BREACHES OF CONFIDENTIALITY, INDEMNIFICATION OBLIGATIONS, OR GROSS NEGLIGENCE, FOR WHICH LIABILITY SHALL BE UNLIMITED.
```

**CORRECT edit (tight, surgical):**
```
IN NO EVENT SHALL EITHER PARTY'S LIABILITY EXCEED TWELVE (12) MONTHS OF FEES PAID OR PAYABLE HEREUNDER.
```
Script can find and match this in DOCX.

**INCORRECT edit (reformatted):**
```
In no event shall either party's liability exceed twelve (12) months
of fees paid or payable hereunder.
```
Changed case, added line break - script may fail to find original text.

## Verifying Before Generation

Before running redline.py:

1. Count your changes
2. Each change should be a specific clause replacement
3. Diff the files to confirm only intended changes:
   ```bash
   diff .claude/workspace/working/contract_work.md \
        .claude/workspace/working/contract_work_copy.md
   ```
