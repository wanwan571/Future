# စတင်ရန် — Perfume Project ကို Claude account အသစ်မှာ ပြန်တည်နည်း

ဒီ folder ထဲမှာ project တစ်ခုလုံး ပါပါတယ် — Studio app code၊ ရေမွေး data၊ ရေမွေးတစ်လုံးချင်း
အချက်အလက် (markdown)၊ design၊ chat က ရေမွေးရှာတဲ့ skill နဲ့ Claude လိုက်နာရမယ့် စည်းကမ်းတွေ။
Account ဟောင်းထဲက ဘာမှ မပျက်ပါဘူး — account အသစ်မှာ မိတ္တူ တစ်ခု ထပ်တည်တာပါ။

## ဘာတွေ ပါလဲ

```
START-HERE.md              ← ဒီ file
README.md                  ← project အကျဉ်း၊ နေ့စဉ် သုံးနည်း
CLAUDE.md                  ← Claude Code က အလိုလို ဖတ်တဲ့ စည်းကမ်း
PROJECT-INSTRUCTIONS.md    ← claude.ai Project ရဲ့ Instructions ထဲ ကူးထည့်ဖို့
project.json               ← Studio link၊ design link
studio/
  perfume-research-studio.html   ← Studio app code အပြည့်
  capabilities.json              ← Studio သုံးခွင့်တွေ (AI၊ database၊ web ရှာ၊ download)
  STUDIO-GUIDE.md                ← ခလုတ်တွေ၊ data ပုံစံ၊ AI prompt တွေ ရှင်းပြချက်
data/
  perfume-studio-backup.json     ← ရေမွေး ၄ လုံးလုံး (Studio ထဲ Import လုပ်ဖို့)
  perfumes/<ရေမွေး>.json          ← တစ်လုံးချင်း backup
perfumes/<ရေမွေး>.md              ← တစ်လုံးချင်း အချက်အလက် + script + caption အကုန် (ဖတ်ဖို့)
design/                          ← ဖုန်း design canvas
.claude/skills/perfume-research/ ← chat က ရေမွေးရှာပြီး Studio ထဲ သိမ်းတဲ့ skill
tools/                           ← backup ခွဲတာ၊ markdown ထုတ်တာ
perfume-research-skill.zip       ← claude.ai Skills ထဲ upload လုပ်ဖို့ (zip ထဲမှာပဲ ပါ)
```

ရေမွေး data ၄ လုံး:
- **Louis Vuitton Moon Tale Eau de Parfum** — Studio ထဲမှာ web နဲ့ ရှာထား၊ script အကုန် ပါ
- **Dior Sauvage Eau de Parfum** — Studio ထဲမှာ web နဲ့ ရှာထား၊ script အကုန် ပါ
- **Versace Pour Homme Dylan Blue EDT** နဲ့ **Yves Saint Laurent Y EDP** — Chat က source နဲ့
  စစ်ထားတဲ့ အချက်အလက်၊ script မထုတ်ရသေး — Studio မှာ ဖွင့်တာနဲ့ အလိုလို ရေးပေးမယ်

## နည်း ၁ — claude.ai Project (GitHub မလို)

1. claude.ai → **Projects** → **New project** — နာမည် "Perfume Review Studio"။
2. **Instructions** ထဲကို `PROJECT-INSTRUCTIONS.md` ရဲ့ `---` အောက်က စာ အကုန် ကူးထည့်ပါ။
3. **Project knowledge** ထဲ upload လုပ်ပါ:
   - `perfumes/` ထဲက ရေမွေး `.md` ၄ ခု
   - `studio/STUDIO-GUIDE.md`
   - `.claude/skills/perfume-research/schema.md` နဲ့ `example.json`
4. (ရရင်) Settings → Capabilities → Skills မှာ `perfume-research-skill.zip` ကို upload လုပ်ပါ။
5. Chat မှာ **Web search** ဖွင့်ထားပါ (ရေမွေး ရှာဖို့ လိုတယ်)။

**သုံးနည်း**
- Project ထဲ chat အသစ်ဖွင့်ပြီး ရေမွေးနာမည် ရိုက်ပါ → Claude က web မှာ ရှာ၊ source နဲ့ စစ်ပြီး
  အချက်အလက် အပြည့်ကို `.md` file အဖြစ် ပေးပါမယ်။ အဲဒီ file ကို Project knowledge ထဲ ထပ်တင်ထားရင်
  နောက် chat တွေကလည်း သိနေပါမယ်။
- "Script ရေးပေး"၊ "Caption ရေးပေး"၊ "ဘယ်လိုပြောရမလဲ" လို့ မေးရင် knowledge ထဲက အချက်အလက်ပေါ်ကပဲ
  ရေးပေးပါမယ်။ ရေမွေး ၄ လုံးရဲ့ script တွေက `.md` file ထဲမှာ ရှိပြီးသားပါ (Dylan Blue နဲ့ YSL Y မှာ
  script မပါသေးလို့ chat မှာ ရေးခိုင်းပါ)။

**Studio app ကိုပါ သုံးချင်ရင် (မဖြစ်မနေ မဟုတ်)**
1. Project ထဲ chat မှာ `studio/perfume-research-studio.html` ကို upload လုပ်ပြီး
   "ဒီ HTML file ကို code မပြင်ဘဲ artifact အဖြစ် ဖွင့်ပေး" လို့ ပြောပါ။
2. Studio ပွင့်ရင် → Library → 💾 Backup → Import → `perfume-studio-backup.json` ရွေးပါ။
3. ⚠️ Studio က AI၊ database၊ web ရှာ capability တွေ လိုပါတယ်။ Chat သာမန်ရဲ့ artifact မှာ ဒါတွေ
   ရမရ ကျွန်တော် မစစ်နိုင်ပါ။ "AI မသုံးနိုင်ပါ" ပေါ်ရင်၊ ဒါမှမဟုတ် Import လုပ်တာ မသိမ်းရင် အဲဒီ
   chat မှာ Studio မရပါဘူး — Project chat (အပေါ်က သုံးနည်း) နဲ့ပဲ ဆက်သုံးပါ၊ info နဲ့ script
   အကုန် ရပါတယ်။

## နည်း ၂ — Claude Code (GitHub လို၊ Studio အကုန် သေချာ အလုပ်လုပ်)

ဒီ project ကို တည်ဆောက်ခဲ့တဲ့ နည်းပါ။

1. claude.ai → Settings → Connectors → **Parallel Search** ချိတ်ပါ။
2. claude.ai/code ဖွင့်ပြီး GitHub ချိတ်၊ ဒီ folder ကို repo အဖြစ် တင်ပါ။
3. အဲဒီ repo နဲ့ session ဖွင့်ပြီး ပို့ပါ:

   > START-HERE.md ထဲက "Claude လုပ်ရမယ့် အဆင့်" အတိုင်း လုပ်ပေး — Studio ကို ဒီ account မှာ publish လုပ်၊ backup data ထည့်၊ project.json ကို link အသစ်နဲ့ ပြင်ပြီး commit လုပ်ပေး။

4. Studio link ဖွင့် → `Dylan Blue` ရိုက်ရှာ → ပွင့်လာရမယ်။

## Data ကို ကိုယ်တိုင် ထည့်နည်း (Claude မလိုဘူး)

Studio ဖွင့် → အောက်က **Library** → အောက်ဆုံး **💾 Backup** → **⬆️ Import file ရွေးမယ်** →
`data/perfume-studio-backup.json` ရွေး → **"အသစ် ၄ ခု ထည့်မယ်"**။

## Claude လုပ်ရမယ့် အဆင့် (for Claude)

1. Load the `artifact-design` and `artifact-capabilities` skills, then publish
   `studio/perfume-research-studio.html` with the `Artifact` tool as a new artifact:
   `capabilities` = the object in `studio/capabilities.json`, `icon` = `perfume`,
   description "Burmese perfume research and review-script studio". The page has its own `<title>`.
2. Import the data: `python3 tools/split_backup.py data/perfume-studio-backup.json <scratchpad>/import`,
   then `ArtifactData` `set` each printed file (`collection` = `perfumes` or `vs`, `doc_id` = file
   name without `.json`, `file_path` = that file); batch at most 3 documents per call (they are large).
   Check with `ArtifactData` `list` that all 4 perfumes are there.
3. Put the new link in `project.json` → `studio.url`, commit and push.
4. Optional: recreate the design canvas from `design/` (static mockup; not needed to run).
5. Send the user the Studio link in Burmese and remind them to keep Parallel Search connected.

## မပါနိုင်တာ

- ဒီ chat ရဲ့ စကားပြော မှတ်တမ်း၊ artifact version အဟောင်းတွေ — ဆုံးဖြတ်ချက် စည်းကမ်း အကုန်
  `CLAUDE.md` နဲ့ `PROJECT-INSTRUCTIONS.md` ထဲ ရေးထားလို့ အလုပ်လုပ်ပုံ မပြောင်းပါ။
- ရေမွေး ပုံတွေ (အခု data ထဲမှာ ပုံ မရှိပါ)။
- Data က export လုပ်တဲ့နေ့အထိပဲ — Studio ဟောင်းမှာ ထပ်ထည့်ရင် 💾 Export နဲ့ backup အသစ် ထုတ်ပါ။
