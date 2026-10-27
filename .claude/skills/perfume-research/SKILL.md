---
name: perfume-research
description: Research one perfume on the web and save a verified, sourced profile into the seller's ရေမွေး Review Studio artifact database. Use when the user types a perfume or brand name (e.g. "Monegal", "Dior Sauvage EDP", "YSL Y EDP ရှာပေး"), asks to research or re-check a perfume, or says "Studio queue ထဲက ရှာပေး".
---

# Perfume research → Studio

The user is a Burmese-speaking perfume seller who films review videos. This chat does the
research; the Studio artifact stores it and writes scripts, captions and talking points from it.
Your job is the facts only. Do not write scripts here: when the user opens a perfume you saved,
the Studio writes them itself from your facts.

Reply to the user in Burmese.

## 0. Find the Studio

Read `project.json` at the repository root: `studio.url` is the Studio artifact, `studio.collection`
(`perfumes`) is the collection. If that artifact cannot be read from this account (a new account
after an import), run `Artifact` `list`, find the page titled "ရေမွေး Review Studio", update
`project.json`, and tell the user. If there is none, follow `START-HERE.md` first.

No `ArtifactData` tool in this chat (for example a regular claude.ai chat)? Do steps 1, 3, 4 and 5
anyway, then hand the user a file instead of saving (step 6, "file mode").

## 1. Pin down the exact perfume

- A brand alone ("Monegal", "Lattafa") or a name with several versions (EDT / EDP / Parfum /
  Elixir, flankers) is ambiguous. Run one quick `web_search`, list the 4–8 likely perfumes
  (with concentration and year), and ask which one with `AskUserQuestion`. Never guess.
- Several names in one message: do them one after another.

## 2. Check what the Studio already has

`ArtifactData` `list` the `perfumes` collection (use `out_dir` — documents are large).

- Same perfume already saved (same id, or same name and concentration): say so, show its date
  and origin, and ask whether to re-check it. A re-check updates that document (step 6).
- "Studio queue ထဲက ရှာပေး": the queue is every document whose `verifyRequest` is set. Research
  each one and clear `verifyRequest` when you save.

## 3. Research

Use the Parallel Search tools (`mcp__Parallel_Search__web_search`, `web_fetch`; load them with
ToolSearch). Send the independent searches in one turn, one objective each:

1. Facts: official name and concentration, launch year, perfumer, notes pyramid, accords, sizes.
2. Performance and reception: longevity, sillage, season and day/night votes, praise, complaints.
3. Story: campaign faces and photographer/director, slogan, bottle designer, what the name means.
4. Line and versions: flankers with years and how they differ.
5. Buying: official prices and sizes, how to spot a fake.

Then `web_fetch` the Fragrantica and Parfumo pages (accords in order, votes, ratings, perfumer,
pyramid) and the brand's own product page.

Reliability, highest first: brand site / box > Fragrantica, Parfumo, Basenotes > big retailers and
trade press (WWD, Forbes, Cosmetics Business) > reviews and blogs > Reddit. Two independent
reliable sources that agree make a fact certain. Keep only facts about this exact version.
Note every URL you actually used; you may cite only URLs that appeared in your results.

## 4. Write the document

Follow `schema.md` exactly; `example.json` is a complete, correct document (Versace Dylan Blue).

Language rules (the user asked for these; they apply to every text value):
- Burmese for descriptions. Brand, perfume, note and accord names stay in English exactly
  ("Amber", "Bergamot"), never translated or transliterated, no Burmese name next to them.
- Perfume terms in English: Longevity, Projection, Sillage, Top / Heart / Base notes, Dry down,
  Accord ("Longevity ၇–၉ နာရီ", not "ခံချိန်").
- Never write "မြန်မာ", "မြန်မာနိုင်ငံ" or "Myanmar" as a qualifier — the seller and viewers are all
  there ("ရာသီဥတု ပူတဲ့အခါ", not "မြန်မာ ရာသီဥတုမှာ"). "မြန်မာလို" meaning the Burmese language is fine.
- Put ⚠️ inside any sentence you are not sure of, and on facts that come only from your own
  knowledge. Numbers (ratings, votes, prices) only from sources. Never invent quotes or URLs.
- Seasons and sprays are judged for hot, humid weather (နွေ မတ်–မေ, မိုး ဇွန်–အောက်တိုဘာ,
  ဆောင်း နိုဝင်ဘာ–ဖေဖော်ဝါရီ).

Build the JSON with a small Python script (write the file, don't paste huge JSON inline), e.g.
in your scratchpad: `doc = {...}; json.dump(doc, open(path, "w"), ensure_ascii=False, indent=1)`.

## 5. Validate

```
python3 .claude/skills/perfume-research/validate.py /path/to/doc.json
```

Fix everything it reports. It checks keys, types, the 12 deep sections, sources, and the
language rules above.

## 6. Save

Document id = slug of `name`: lowercase, every run of non `[a-z0-9]` characters → `-`, trimmed,
at most 60 characters (`Versace Pour Homme Dylan Blue Eau de Toilette` →
`versace-pour-homme-dylan-blue-eau-de-toilette`).

- New perfume: `ArtifactData` `set` with `file_path` (no `if_version`).
- Re-check of a saved perfume: `ArtifactData` `update` with `if_version` = the version you read.
  Send only the fact fields, `deep`, `compare`, `authenticity`, `faq`, `sources` and the metadata
  (`origin`, `researchedBy`, `verifiedAt`, `webAt`, `updatedAt`, `verifyRequest: null`).
  Never touch `test`, `price`, `status`, `photo`, `archived`, `createdAt` or the script fields
  (`script`, `captions`, `shoot`, `selftest`, `images`, `longscript`, `talk`, `hooks`, `angles`).
  If any of those script fields exist, also send `staleAt` = now, so the Studio offers to rewrite
  them from the new facts.
- File mode (no `ArtifactData`, e.g. a claude.ai Project): give the user the profile as a Markdown
  file `<id>.md` in the same layout as the Project's perfume knowledge files (facts table,
  Accords & Performance, Notes Pyramid, seasons and occasions, pros / cons, brand story, the 12
  deep sections, comparison, fake checks, FAQ, ⚠️ items, sources) and suggest adding it to the
  Project knowledge. Only if they use the Studio app, also give the import file `<id>.json`:
  `{"format": "perfume-review-studio-backup", "version": 1, "exportedAt": "<ISO time>",
  "perfumes": [{...the document..., "id": "<id>"}], "vs": []}` — Studio → Library → 💾 Backup →
  ⬆️ Import → choose the file → "အသစ် ၁ ခု ထည့်မယ်".

## 7. Report (Burmese, short)

- What you saved and the Studio link.
- The 3–5 most useful facts.
- The ⚠️ items the user should know before filming.
- "Studio မှာ ဖွင့်လိုက်တာနဲ့ script၊ ပြောစရာ၊ Post တွေကို ဒီ အချက်တွေပေါ်ကပဲ အလိုလို ရေးပေးပါမယ်။"
