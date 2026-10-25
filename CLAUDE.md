# ရေမွေး Review Studio — project notes for Claude

## Who this is for

A Burmese-speaking perfume seller who reviews perfumes in Facebook Reels / TikTok / YouTube and
sells full bottles and 5ml / 10ml decants. They work mostly on a phone. Always reply in Burmese,
short and plain.

What they want, in their order: correct, complete perfume info → scripts → posts → content ideas
(ဘယ်လိုပြောရမယ်၊ ဘယ်လိုရေးရမယ်). They do NOT want posting schedules, calendars, stock, sales or
post-result tracking.

## What is here

- `studio/perfume-research-studio.html` — the Studio, a claude.ai artifact (one HTML page).
  Its live URL is in `project.json` (`studio.url`). Capabilities: `studio/capabilities.json`.
  Data lives in the artifact's database, collection `perfumes` (one document per perfume) and
  `vs` (saved VS scripts).
- `data/perfume-studio-backup.json` — a backup of that database in the Studio's own format
  (the Studio's Library → 💾 Backup → Import reads it).
- `design/` — the phone-first design canvas the Studio follows (`project.json` → `design.url`).
- `.claude/skills/perfume-research/` — how to research a perfume in chat and save it to the Studio.

## How the pieces work together

1. The user types a perfume name in chat → use the `perfume-research` skill: web research with
   sources, write the document, validate, save it to the Studio database with `researchedBy: "chat"`.
2. In the Studio, searching a saved name opens the saved document (no new research). The first
   time a chat-researched perfume is opened, the Studio writes its scripts, talking points, posts
   and ideas from those facts only (strict grounding in the prompts).
3. Chat-researched facts are protected in the Studio: "rewrite all" keeps the researched info and
   only rewrites scripts; a Studio web re-check only fills empty fields; merging pasted sources
   pre-selects nothing.
4. "Studio queue ထဲက ရှာပေး" = research every document whose `verifyRequest` is set.

## Rules for every text the user sees

- Brand, perfume, note and accord names stay English; no Burmese translation next to them.
- Perfume terms in English: Longevity, Projection, Sillage, Top / Heart / Base, Accords, Day / Night,
  Masculine / Feminine.
- Never write "မြန်မာ" / "Myanmar" as a qualifier; it is understood. ("မြန်မာလို" = in Burmese is fine.)
- Put ⚠️ on anything unsure. Never invent facts, numbers, quotes or URLs.

## Changing the Studio

- Edit `studio/perfume-research-studio.html`, then publish it with the `Artifact` tool to
  `studio.url` (same `file_path` → same URL). Omit `capabilities` on a republish so the stored
  set carries forward. Read the `artifact-design` and `artifact-capabilities` skills first.
- Keep the page's patterns: the `h()` DOM builder, state in `S`, `render()`, `patchDoc` / `setDoc`
  for writes, Burmese UI copy, phone layout (fixed bottom nav, folds, show more / show fewer).
- Test in headless Chromium with a mocked `window.claude.use` before publishing.

## Moving to another account

Follow `README.md` → "တခြား account ထဲ ပြန်ထည့်နည်း". If `studio.url` cannot be read from the
current account, the project has been moved: publish the Studio there, import the backup, and
update `project.json`.
