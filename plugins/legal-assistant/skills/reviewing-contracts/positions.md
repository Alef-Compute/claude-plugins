# Foundational Clause Positions

This is the default reference for contract analysis. Playbooks override specific positions.

## Contents

- [How This Works](#how-this-works)
- [Severity Ratings](#severity-ratings)
- [Clause Positions](#clause-positions)
  - [liability_cap](#liability_cap)
  - [indemnification](#indemnification)
  - [termination](#termination)
  - [payment_terms](#payment_terms)
  - [confidentiality](#confidentiality)
  - [intellectual_property](#intellectual_property)
  - [governing_law](#governing_law)
  - [data_protection](#data_protection)
  - [insurance](#insurance)
  - [force_majeure](#force_majeure)
  - [assignment](#assignment)
  - [warranties](#warranties)
  - [dispute_resolution](#dispute_resolution)
  - [audit_rights](#audit_rights)
  - [mfn_clause](#mfn_clause)

---

## How This Works

1. Use positions.md as baseline for ALL clause analysis
2. If playbook exists, playbook positions OVERRIDE matching clause IDs
3. Clauses not in playbook fall back to these defaults
4. Log which source (playbook vs default) was used for each clause

---

## Severity Ratings

**HIGH** - Deal-breaker. Requires executive/legal approval to accept.
- Unlimited/uncapped liability
- One-sided indemnification for counterparty's negligence
- IP assignment without license-back
- No termination for cause

**MEDIUM** - Negotiate. Push back but not a walk-away.
- Liability cap below 12 months fees
- Missing standard carve-outs
- Auto-renewal without 60+ day notice

**LOW** - Flag. Note for awareness.
- Minor deviations from preference
- Missing "nice to have" protections

---

## Clause Positions

### liability_cap

**Look for:** Cap amount, scope (all claims vs carve-outs), symmetry

**Red flags:**
- Unlimited liability → HIGH
- Cap below 12 months fees → MEDIUM
- Asymmetric caps favoring counterparty → MEDIUM

**Default position:** 12 months fees, mutual, carve-outs for IP/confidentiality/indemnity

**Sample language:**

Balanced:
> Neither party's aggregate liability shall exceed the fees paid or payable in the twelve (12) months preceding the claim.

Buyer-favorable:
> Vendor's aggregate liability shall not exceed fees paid in the six (6) months preceding the claim.

Vendor-favorable:
> Liability shall not exceed the fees paid for the specific service giving rise to the claim.

---

### indemnification

**Look for:** Scope, carve-outs, cap, defense/control procedures

**Red flags:**
- One-sided (only customer indemnifies) → HIGH
- Uncapped indemnification → HIGH
- Covers counterparty's own negligence → HIGH
- No standard IP infringement coverage → MEDIUM

**Default position:** Mutual for IP infringement and third-party claims arising from breach

**Sample language:**

Balanced:
> Each party shall indemnify the other against third-party claims arising from: (a) its breach of this Agreement, (b) its negligence or willful misconduct, and (c) infringement of third-party IP rights by materials it provides.

Buyer-favorable:
> Vendor shall indemnify Customer against all claims arising from: (a) the Services, (b) Vendor's breach, (c) IP infringement, and (d) data breaches caused by Vendor.

---

### termination

**Look for:** For-cause triggers, notice periods, cure periods, convenience termination

**Red flags:**
- No termination for cause → HIGH
- No cure period for material breach → MEDIUM
- Notice period under 30 days → MEDIUM
- Auto-renewal without 60+ day opt-out → MEDIUM

**Default position:** Mutual for-cause with 30-day notice and 30-day cure; annual term with 60-day renewal notice

**Sample language:**

Balanced:
> Either party may terminate for material breach if uncured within thirty (30) days of written notice. Either party may terminate for convenience with ninety (90) days written notice.

Buyer-favorable:
> Customer may terminate for convenience with thirty (30) days notice. Vendor may terminate only for Customer's material breach uncured within sixty (60) days.

---

### payment_terms

**Look for:** Payment timing, late fees, disputes, price increases

**Red flags:**
- Payment on signing (before delivery) → MEDIUM
- Late fees exceeding 1.5%/month → LOW
- No right to dispute invoices → MEDIUM
- Uncapped annual price increases → MEDIUM

**Default position:** Net-30 payment, 1%/month late fee, invoice dispute rights, price increases capped or with notice

**Sample language:**

Balanced:
> Payment due within thirty (30) days of invoice. Late payments accrue interest at 1% per month. Customer may dispute invoices in good faith within fifteen (15) days.

---

### confidentiality

**Look for:** Duration, scope, carve-outs, return/destruction

**Red flags:**
- Perpetual obligation with no carve-outs → MEDIUM
- No standard carve-outs (public info, independent development) → MEDIUM
- One-sided (only one party bound) → MEDIUM

**Default position:** Mutual, 3-5 years post-termination, standard carve-outs

**Sample language:**

Standard carve-outs:
> Confidential Information excludes information that: (a) is or becomes public through no fault of recipient, (b) was known to recipient prior to disclosure, (c) is independently developed without use of Confidential Information, or (d) is disclosed by a third party without restriction.

---

### intellectual_property

**Look for:** Ownership of deliverables, license grants, work-for-hire, background IP

**Red flags:**
- Customer assigns all IP to vendor → HIGH
- Work-for-hire without license-back → HIGH
- No license to use deliverables → MEDIUM
- Vendor retains rights to customer data derivatives → MEDIUM

**Default position:** Customer owns custom deliverables; vendor retains background IP with perpetual license to customer

**Sample language:**

Balanced:
> Customer owns all custom deliverables. Vendor retains ownership of pre-existing IP and grants Customer a perpetual, non-exclusive license to use such IP as incorporated in deliverables.

---

### governing_law

**Look for:** Jurisdiction, venue, choice of law

**Red flags:**
- Foreign jurisdiction → MEDIUM (unless business reason)
- Mandatory arbitration without opt-out → LOW
- Inconvenient venue → LOW

**Default position:** Governing law of customer's principal place of business, courts of that jurisdiction

**Sample language:**

Balanced:
> This Agreement shall be governed by the laws of [State], without regard to conflict of laws principles. The parties consent to exclusive jurisdiction in the state and federal courts located in [County, State].

---

### data_protection

**Look for:** DPA requirements, data location, breach notification, subprocessors

**Red flags:**
- No DPA for personal data processing → HIGH
- No breach notification timeline → MEDIUM
- Unlimited subprocessor rights → MEDIUM
- Data stored outside approved jurisdictions → MEDIUM

**Default position:** Standard DPA, 72-hour breach notification, subprocessor approval rights, data localization per regulations

**Sample language:**

> Vendor shall notify Customer of any data breach within seventy-two (72) hours of discovery. Vendor shall not engage subprocessors without Customer's prior written consent.

---

### insurance

**Look for:** Coverage types, limits, additional insured status

**Red flags:**
- No cyber/E&O coverage for tech services → MEDIUM
- Coverage limits below industry standard → LOW
- No certificate of insurance requirement → LOW

**Default position:** GL $1M, E&O/Cyber $2M, Workers Comp statutory

**Sample language:**

> Vendor shall maintain: (a) Commercial General Liability of $1,000,000 per occurrence, (b) Professional Liability/E&O of $2,000,000, (c) Cyber Liability of $2,000,000, and (d) Workers Compensation at statutory limits.

---

### force_majeure

**Look for:** Covered events, notice requirements, termination rights

**Red flags:**
- Includes economic hardship or labor disputes → LOW
- No termination right after extended force majeure → MEDIUM
- Only excuses one party → LOW

**Default position:** Standard events (natural disasters, war, government action), mutual, termination right after 30-90 days

**Sample language:**

> Neither party shall be liable for delays due to causes beyond reasonable control, including natural disasters, war, terrorism, or government action. If force majeure continues beyond sixty (60) days, either party may terminate without liability.

---

### assignment

**Look for:** Consent requirements, change of control, successors

**Red flags:**
- Vendor can assign without consent → MEDIUM
- No change of control provision → LOW
- Assignment to competitor permitted → MEDIUM

**Default position:** No assignment without consent, except to affiliate or in M&A with notice

**Sample language:**

Balanced:
> Neither party may assign without prior written consent, except to an affiliate or successor in a merger or acquisition, provided written notice is given within thirty (30) days.

---

### warranties

**Look for:** Performance standards, compliance, non-infringement, disclaimers

**Red flags:**
- Complete disclaimer of all warranties → MEDIUM
- No compliance warranty → MEDIUM
- No IP non-infringement warranty → MEDIUM

**Default position:** Warranties for performance to specifications, compliance with laws, non-infringement of third-party IP

**Sample language:**

> Vendor warrants that: (a) Services will perform materially as described in the documentation, (b) Services will comply with applicable laws, and (c) Services will not infringe third-party intellectual property rights.

---

### dispute_resolution

**Look for:** Escalation process, mediation/arbitration, venue, fees

**Red flags:**
- Immediate arbitration without negotiation → LOW
- Arbitration in inconvenient venue → LOW
- Loser pays all fees → MEDIUM

**Default position:** Executive escalation, then mediation, then litigation/arbitration; each party bears own costs

**Sample language:**

> Prior to litigation, disputes shall be escalated to executive sponsors for thirty (30) days of good faith negotiation. If unresolved, parties shall attempt mediation before proceeding to binding arbitration.

---

### audit_rights

**Look for:** Scope, frequency, notice, cost allocation

**Red flags:**
- No audit rights for compliance → MEDIUM (especially for regulated industries)
- Unlimited audit frequency → LOW
- Customer bears all audit costs → LOW

**Default position:** Annual audit with 30-day notice, customer bears cost unless material non-compliance found

**Sample language:**

> Customer may audit Vendor's compliance with this Agreement once annually with thirty (30) days notice. Customer bears audit costs unless audit reveals material non-compliance, in which case Vendor bears costs.

---

### mfn_clause

**Look for:** Scope (pricing, terms), comparison group, remedy

**Red flags:**
- No MFN for volume customer → LOW (nice to have)
- MFN limited to pricing only → LOW

**Default position:** Pricing MFN for similarly-situated customers, with right to retroactive adjustment

**Sample language:**

> Vendor represents that pricing and terms are no less favorable than those offered to similarly-situated customers. If Vendor offers more favorable terms to a similar customer, Customer shall be entitled to such terms retroactively.
