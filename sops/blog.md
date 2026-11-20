# SOP — Blog Post

**Time limit:** 1 day max. Urgent cuts to hours, Low stretches a bit.
**Gate:** the system runs this SOP's checks before the card reaches the Inspector. Fail goes back to the builder with the exact failed check. Nothing reaches the Inspector unproven.

## Inputs (the card must have these)
- Title, description, category.
- Requirements (prewritten on the card): peer-reviewed sources, shareable, house blog style, own card art.

## Steps
1. **Research.** Find peer-reviewed sources for every claim that needs one. Keep the links.
2. **Draft.** Write it in the house style: big type, minimal words, one focus per screen. Shareable — a reader should want to send it to someone.
3. **Art.** Make its own card art (.jpg/.png, in `/img/cards/`). No fallback or placeholder image, ever.
4. **Build the page.** `.html`, lowercase hyphenated file name matching the slug. Blog goes in `/journal/` (standalone posts keep their agreed root URL).
5. **Meta.** Title, description, canonical, og tags, twitter card, BlogPosting data. Blog tags and category set.
6. **Self-check.** Run the checks below yourself before you upload. Log what you did, what you tested, what you didn't test.
7. **Upload.** Right repo, right branch. Note the commit hash, who did it, when, and what changed.
8. **Live check.** Open the live URL. It must return 200 — no redirect to a dead project.

## Gate checks (system runs these)
- [ ] File exists in the repo + commit hash present.
- [ ] Live URL returns 200.
- [ ] Desktop + mobile render PASS.
- [ ] All links on the page work — including every peer-reviewed source link.
- [ ] Same site design / header-footer present.
- [ ] Peer-reviewed source links present and working.
- [ ] Shareable (share links present, house blog style).
- [ ] Correct file type (.html) and folder (/journal/ or agreed root URL).
- [ ] Meta / og / canonical present; blog tags and category right.
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
