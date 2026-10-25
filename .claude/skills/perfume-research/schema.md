# Studio perfume document (`perfumes/<id>`)

One JSON object per perfume. Text is Burmese unless the field says English. See `example.json`.

## Metadata

| field | value |
|---|---|
| `v` | `2` |
| `origin` | `"web"` |
| `researchedBy` | `"chat"` — makes the Studio show 🔬, protect these facts and write scripts on first open |
| `status` | `"research"` for a new perfume (keep the existing value on a re-check) |
| `createdAt`, `updatedAt`, `verifiedAt`, `webAt` | now, in milliseconds since 1970 (`int(time.time()*1000)`) |
| `verifyRequest` | `null` |
| `price` | `""` (the seller fills it) |
| `test` | `{}` (the seller's own wear test) |
| `query` | what the user typed |
| `name`, `title` | full English name: brand + perfume + concentration, e.g. `"Yves Saint Laurent Y Eau de Parfum"` |

## Facts

| field | type | content |
|---|---|---|
| `brand` | string | English |
| `concentration` | string | `EDT` / `EDP` / `Parfum` / `Elixir` / `Extrait` / `Cologne` |
| `year` | string | `"2018"`; ⚠️ if sources disagree |
| `perfumer` | string | English names, `·` between several |
| `family` | string | English, e.g. `"Aromatic Fougère"` |
| `gender` | string | e.g. `"ယောကျ်ားလေး (Men)"`, `"အမျိုးသမီး (Women)"`, `"Unisex"` |
| `sizes` | string | `"30ml · 50ml · 100ml"` |
| `bottle` | string | what the bottle looks like |
| `longevity_text` | string | hours in Burmese digits, e.g. `"၆–၈ နာရီ"` |
| `projection_text` | string | 1–3 Burmese words |
| `ref_price` | string | official prices with currency, size and where; ⚠️ |
| `concept_title` | string | campaign idea in a few words (English is fine) |
| `concept` | string | 2–4 sentences: brand story, faces, what the name means |
| `one_liner` | string | the whole scent in one vivid sentence |
| `verdict` | string | who it suits + its main weakness, one sentence |
| `target` | string | age, style, beginner or collector |
| `myanmar_tip` | string | how it behaves in heat and humidity and how many sprays (the key name stays; never write "မြန်မာ" in the text) |
| `hook` | string | one idea or fact for the first 3 seconds of a video |
| `alternatives` | string[] | other versions, English names |
| `accords` | `{name, pct}[]` | up to 8, lowercase English names in Fragrantica's order; `pct` 5–100 (Fragrantica's accords-search link carries the numbers) |
| `meters` | object | `longevity` 1–5, `projection` 1–5, `sweetness` 1–5, `day` 0–100 (% day votes), `masculine` 0–100 |
| `phases` | object[] | 3 items: `{stage: "Top"/"Heart"/"Base", start_h, end_h, time_text, feel, analogy, summary: "Note · Note"}`; Base `end_h` = realistic total hours |
| `notes` | object[] | `{stage: "Top"/"Heart"/"Base", note: English, smell: Burmese comparison, certain: bool}`; `certain: false` when sources disagree |
| `seasons` | object[] | exactly 3: `{season: "နွေ"/"မိုး"/"ဆောင်း", months: "မတ်–မေ"/"ဇွန်–အောက်တိုဘာ"/"နိုဝင်ဘာ–ဖေဖော်ဝါရီ", fit: 1–5, sprays, advice}` |
| `occasions` | object[] | 6–7: `{occasion, fit: 1–5, note}` — ရုံး, ကျောင်း / University, နေ့စဉ်, Date, ညပွဲ / ပါတီ, လက်ဆောင်, နေပူထဲ / အားကစား |
| `pros`, `cons` | string[] | 4–5 each, honest |
| `uncertain` | string[] | each starts with ⚠️: what sources disagree on or could not confirm |
| `verify` | string[] | 2–4 things the seller should check themselves |

Meters from community data: Parfumo longevity/sillage out of 10 → roughly ÷2; Fragrantica
`day` = day votes ÷ (day + night) × 100.

## Info sections

`deep`: exactly 12 objects `{key, title, body, bullets}` in this order. `body` is 120–200 Burmese
words, paragraphs separated by `\n\n`; `bullets` is `[]` unless noted.

| key | title | content |
|---|---|---|
| `history` | ထွက်ရှိမှုနဲ့ ဇာတ်လမ်း | launch, the brand's situation, rivals then, reception, ratings |
| `perfumer` | ဖန်တီးသူ | who, other work (⚠️ if from memory), style, one line to say on video |
| `design` | ပုလင်းနဲ့ ထုပ်ပိုးမှု | bottle, designer, cap, box, sizes, batch code place |
| `campaign` | ကြော်ငြာနဲ့ မျက်နှာ | faces and directors by year, slogan, a video hook idea |
| `name` | နာမည်ရဲ့ အဓိပ္ပါယ် | meaning, names people confuse |
| `notes_detail` | Note တစ်ခုချင်း အသေးစိတ် | short intro; bullets: one per note top→base, "Note — what it is, smell, role, when noticeable" |
| `journey` | အနံ့ခရီး မိနစ်အလိုက် | one intro sentence; bullets "၀–၅ မိနစ်: …", "၅–၃၀ မိနစ်: …", "၃၀ မိနစ် – ၂ နာရီ: …", "၂–၅ နာရီ: …", "၅ နာရီ+: …" |
| `performance` | Longevity & Projection | community numbers, skin vs clothes, heat / AC / rain, sprays, reformulation talk |
| `audience` | ဘယ်သူ ဘယ်အချိန် | age, style, occasions with scores, season votes, who should not buy, clothes |
| `community` | Community အမြင် | praise, criticism, compliments, how common |
| `versions` | Line ထဲက version တွေ | one intro sentence; bullets: one per version "Name (year) — how it differs"; last bullet "ဘာကို ဝယ်မလဲ — …" |
| `buying` | ဝယ်ယူမှု အကြံပြုချက် | prices, decant advice, fake summary, what not to claim |

`compare`: 5–7 rows `{name, group, year, character, fresh, sweet, strength, longevity, best_for, is_self}`.
First row is this perfume with `is_self: true` and `group: "ဒီရေမွေး"`; then versions of the same
line (`"Line ထဲက version"`), then rivals (`"ယှဉ်ပြိုင်ဘက်"`), at most one cheaper look-alike
(`"ဈေးသက်သာ အလားတူ"`). `fresh`, `sweet`, `strength` are integers 1–5.

`authenticity`: 5–7 rows `{area, check, red_flag}` specific to this bottle.

`faq`: 6 rows `{q, a}` customers really ask (EDT vs EDP, how long it lasts, hot weather, versions,
real vs fake, decant size). Answers may use the Studio's blanks `{HOURS}`, `{PRICE_FULL}`,
`{PRICE_10ML}`, `{PRICE_5ML}`.

`sources`: 3–10 objects `{label: site name, topic: Burmese — which facts it supports, url}`;
`https://` URLs you actually saw in search or fetch results.
