# SOP — Top 5 (Starting Lineup)

**Time limit:** 1 day max. Urgent cuts to hours, Low stretches a bit.
**Gate:** the system runs this SOP's checks before the card reaches the Inspector. Fail goes back to the builder with the exact failed check. Nothing reaches the Inspector unproven.

## Inputs (the card must have these)
- Category (all 5 picks are the SAME category — not 5 random things).
- Requirements (prewritten on the card): exactly 5 picks, same category, every pick on Amazon with the tag, own card art.

## Steps
1. **Pick 5.** Same category, same kind. Each pick must draw attention and have a way to be advertised and a way to make money. A pick that fails any of the three is out.
2. **Verify Amazon.** Every pick must be sold on Amazon with a "See Amazon price" link carrying tag `leonlink-20`. A pick that is not on Amazon leaves the list — removed, no exceptions. Never a search URL, always the product link.
3. **Write it up.** Short, plain, one focus per pick. House style.
4. **Art.** Make its own card art (.jpg/.png, in `/img/cards/`). No fallback or placeholder image, ever.
5. **Build the page.** `.html`, lowercase hyphenated file name matching the slug. Top 5 goes in `/lineup/`.
6. **Meta.** Title, description, canonical, og tags. List tags and category set.
7. **Self-check.** Run the checks below yourself before you upload. Log what you did, what you tested, what you didn't test.
8. **Upload.** Right repo, right branch. Note the commit hash, who did it, when, and what changed.
9. **Live check.** Open the live URL. It must return 200 — no redirect to a dead project.

## Gate checks (system runs these)
- [ ] File exists in the repo + commit hash present.
- [ ] Live URL returns 200.
- [ ] Desktop + mobile render PASS.
- [ ] All links on the page work.
- [ ] Same site design / header-footer present.
- [ ] Exactly 5 picks — not 4, not 6. A list that drops below five gets flagged, never silently refilled.
- [ ] All 5 picks same category.
- [ ] Every pick has an Amazon "See Amazon price" link with tag `leonlink-20`. A non-Amazon pick fails.
- [ ] Correct file type (.html) and folder (`/lineup/`).
- [ ] Meta / og / canonical present; Amazon tag on every pick.
- [ ] No duplicate title or slug.
- [ ] File name lowercase, hyphens, no spaces, matches the slug.
- [ ] No secrets or personal info (Leon: first name + state only; nothing about the kids).
- [ ] Images owned or generated, not lifted. Alt text on every image.
- [ ] Own card art present in `/img/cards/` — no fallback image.
- [ ] Attribution collected: bot name, team, card number, what changed, when, commit hash.
- [ ] Log with the upload: did / tested / didn't test.

## Done
All checks pass → Inspector review. Inspector passes → Done. Inspector fails → back to Step 1 with the note.

## Fail
Any check fails → the card goes back to the builder with the exact failed check listed. It never reaches the Inspector.
