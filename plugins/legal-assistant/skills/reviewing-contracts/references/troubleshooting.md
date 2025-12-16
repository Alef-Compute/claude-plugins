# Troubleshooting

## Document Conversion Issues

**File not found:**
- Verify the file path is correct
- Check file exists: `ls -la <path>`

**Password-protected PDF:**
- Ask user for password or unprotected version

**Scanned/image-based PDF:**
- Warn user: OCR quality may affect accuracy
- Consider asking for DOCX version if available

**DOCX conversion fails:**
- Check for corrupted file
- Check for macros (may need to save as .docx without macros)

## Redline Generation Issues

**"Text not found" warnings:**
- Check for formatting differences:
  - Smart quotes ("") vs straight quotes ("")
  - Em-dashes (—) vs double-hyphens (--)
  - Non-breaking spaces
- Verify the text exists in original DOCX exactly as shown in markdown
- Try with smaller text segments

**Track changes not visible in Word:**
- Open document in Microsoft Word (not preview)
- Go to Review tab → Track Changes → All Markup
- Check document isn't in "Final" view mode

**Large documents fail:**
- Process in sections if memory issues
- Consider splitting very long contracts

## Playbook Issues

**Invalid playbook format:**
- Check YAML frontmatter has required fields (name, type, risk_tolerance)
- Verify clause IDs match positions.md (use exact IDs)

**Missing clauses:**
- Offer to generate missing clauses from positions.md defaults
- Ask user if they want to add custom position

**Playbook not found:**
- Check `playbooks/` directory exists
- Verify file naming: `playbooks/default.md` or `playbooks/<client>.md`

## Quality Verification

**Output file empty or very small:**
- Redline generation may have failed silently
- Check for error messages in console output
- Verify original DOCX is valid

**Changes not applied correctly:**
- Review the diff between original and modified markdown
- Ensure text changes are surgical (no reformatting)
- Try running with `--verbose` flag if available
