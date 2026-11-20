# SOP — Game

**Time limit:** 3 days, in checkpoints. Urgent cuts to hours, Low stretches a bit.
**Gate:** the system runs this SOP's checks on every upload — including checkpoint uploads — before the card reaches the Inspector. Fail goes back to the builder with the exact failed check. Nothing reaches the Inspector unproven.

## Inputs (the card must have these)
- Title, description, category.
- Graphics specs (style, colors, art, layout) and audio specs (music, sounds).
- Requirements (prewritten on the card): ~5s loading screen, loads and plays, mobile-first, own card art.

## Steps
1. **Day 1 — Draft.** The game exists and runs. Core loop in place, even if rough. Upload checkpoint 1. Checkpoint proof must show real progress, not the same file re-uploaded.
2. **Day 2 — Playable.** The game is playable start to finish. Controls work on mobile. Upload checkpoint 2.
3. **Day 3 — Polish + live check.** Loading screen, art, audio, mobile polish. Then run the checks below, upload, and live-check it.
4. **Loading screen.** Every game opens with a ~5-second `LEONLINK PRESENTS` screen — logo or a spinning item — then the game name. No exceptions.
5. **Art + audio.** Own card art (.jpg/.png, in `/img/cards/`). Graphics and audio owned or generated, not lifted. No fallback or placeholder image, ever.
6. **Build the page.** `.html`, lowercase hyphenated file name matching the slug. Games go in `/games/`.
7. **Meta.** Title, description, canonical, og tags.
8. **Self-check.** Run the checks below yourself before every upload. Log what you did, what you tested, what you didn't test.
9. **Upload.** Right repo, right branch. Note the commit hash, who did it, when, and what changed.
10. **Live check.** Open the live URL. It must return 200 — no redirect to a dead project.

## Gate checks (system runs these, on every upload)
- [ ] File exists in the repo + commit hash present.
- [ ] Live URL returns 200.
- [ ] Desktop + mobile render PASS. Mobile-first: it must play on a phone.
- [ ] All links on the page work.
- [ ] Same site design / header-footer present.
- [ ] ~5s `LEONLINK PRESENTS` loading screen present, then the game name.
- [ ] Game loads and plays.
- [ ] Correct file type (.html; images .jpg/.png only) and folder (`/games/`, images `/img/cards/`).
- [ ] Meta / og / canonical present.
- [ ] No duplicate title or slug.
- [ ] File name lowercase, hyphens, no spaces, matches the slug.
- [ ] No secrets or personal info (Leon: first name + state only; nothing about the kids).
- [ ] Images and audio owned or generated, not lifted. Alt text on every image.
- [ ] Own card art present in `/img/cards/` — no fallback image.
- [ ] Attribution collected: bot name, team, card number, what changed, when, commit hash.
- [ ] Log with the upload: did / tested / didn't test.
- [ ] Checkpoint proof: real progress since the last upload.
- [ ] Page and image size within limits; deploy count respected (stop at 85 a day).

## Done
All checks pass → Inspector review. Inspector passes → Done. Inspector fails → back to work with the note.

## Fail
Any check fails → the card goes back to the builder with the exact failed check listed. It never reaches the Inspector. If the live check fails after deploy, flag it and don't leave a broken page live — roll back.
