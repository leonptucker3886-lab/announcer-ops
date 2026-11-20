# SOP — Software / App

**Time limit:** 7 days, in checkpoints. Urgent cuts to hours, Low stretches a bit.
**Gate:** the system runs this SOP's checks on every upload — including checkpoint uploads — before the card reaches the Inspector. Fail goes back to the builder with the exact failed check. Nothing reaches the Inspector unproven.

## Inputs (the card must have these)
- Title, description, category.
- Requirements (prewritten on the card): loads, core flow works, no login button / no site chrome inside the app, own card art.

## Steps
1. **Day 2 — First working build.** The app loads and the main screen renders. Upload checkpoint 1. Checkpoint proof must show real progress, not the same file re-uploaded.
2. **Day 4 — Core flow working.** The main thing the app does works end to end. Upload checkpoint 2.
3. **Day 7 — Polish + live check.** Polish, edge cases, mobile. Then run the checks below, upload, and live-check it.
4. **No login inside the app.** One central login only — no login buttons in the app, no site nav/chrome inside software apps. (LeonLink ID law.)
5. **White-label ready.** Where the job calls for it, options and features are set by the seller, not fixed monthly tiers.
6. **Art.** Own card art (.jpg/.png, in `/img/cards/`). No fallback or placeholder image, ever.
7. **Build the page.** `.html`, lowercase hyphenated file name matching the slug. Apps go in their agreed folder.
8. **Meta.** Title, description, canonical, og tags.
9. **Self-check.** Run the checks below yourself before every upload. Log what you did, what you tested, what you didn't test.
10. **Upload.** Right repo, right branch. Note the commit hash, who did it, when, and what changed.
11. **Live check.** Open the live URL. It must return 200 — no redirect to a dead project.

## Gate checks (system runs these, on every upload)
- [ ] File exists in the repo + commit hash present.
- [ ] Live URL returns 200.
- [ ] Desktop + mobile render PASS.
- [ ] All links on the page work.
- [ ] Same site design / header-footer present.
- [ ] App loads; core flow works.
- [ ] No login button / no site chrome inside the app.
- [ ] Correct file type (.html; images .jpg/.png only) and folder.
- [ ] Meta / og / canonical present.
- [ ] No duplicate title or slug.
- [ ] File name lowercase, hyphens, no spaces, matches the slug.
- [ ] No secrets or personal info (Leon: first name + state only; nothing about the kids).
- [ ] Images owned or generated, not lifted. Alt text on every image.
- [ ] Own card art present in `/img/cards/` — no fallback image.
- [ ] Attribution collected: bot name, team, card number, what changed, when, commit hash.
- [ ] Log with the upload: did / tested / didn't test.
- [ ] Checkpoint proof: real progress since the last upload.
- [ ] Page and image size within limits; deploy count respected (stop at 85 a day).

## Done
All checks pass → Inspector review. Inspector passes → Done. Inspector fails → back to work with the note.

## Fail
Any check fails → the card goes back to the builder with the exact failed check listed. It never reaches the Inspector. If the live check fails after deploy, flag it and don't leave a broken page live — roll back.
