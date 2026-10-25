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
  perfume-studio-backup.json     ← ရေမွေး ၃ လုံးလုံး (Studio ထဲ Import လုပ်ဖို့)
  perfumes/<ရေမွေး>.json          ← တစ်လုံးချင်း backup
perfumes/<ရေမွေး>.md              ← တစ်လုံးချင်း အချက်အလက် + script + caption အကုန် (ဖတ်ဖို့)
design/                          ← ဖုန်း design canvas
.claude/skills/perfume-research/ ← chat က ရေမွေးရှာပြီး Studio ထဲ သိမ်းတဲ့ skill
tools/                           ← backup ခွဲတာ၊ markdown ထုတ်တာ
perfume-research-skill.zip       ← claude.ai Skills ထဲ upload လုပ်ဖို့ (zip ထဲမှာပဲ ပါ)
```

ရေမွေး data: **Dior Sauvage Eau de Parfum** (script အကုန် ပါ)၊ **Versace Pour Homme Dylan Blue EDT**
နဲ့ **Yves Saint Laurent Y EDP** (Chat က source နဲ့ စစ်ထားတဲ့ အချက်အလက် — Studio မှာ ဖွင့်တာနဲ့
script တွေ အလိုလို ရေးပေးမယ်)။

## နည်း ၁ — Claude Code (အကြံပြု၊ အကုန် အလုပ်လုပ်)

ဒီ project ကို တည်ဆောက်ခဲ့တဲ့ နည်းပါ — Studio app (AI၊ database၊ web ရှာ) နဲ့ chat research
အကုန် သေချာ အလုပ်လုပ်ပါတယ်။

1. **Parallel Search ချိတ်** — account အသစ်မှာ claude.ai → Settings → Connectors → Parallel Search။
2. **GitHub ချိတ်** — claude.ai/code ဖွင့်ပြီး GitHub account ချိတ်ပါ။
3. **File တင်** — ဒီ folder ကို GitHub repo အဖြစ် တင်ပါ (repo အသစ် ဆောက်ပြီး file အကုန် upload၊
   ဒါမှမဟုတ် `wanwan571/Future` repo ရဲ့ branch `claude/sleepy-turing-jqeh9s` ကို သုံး)။
4. **Session ဖွင့်** — claude.ai/code မှာ အဲဒီ repo နဲ့ session အသစ် ဖွင့်ပါ။
5. **ဒီစာကို ကူးပြီး ပို့ပါ:**

   > START-HERE.md ထဲက "Claude လုပ်ရမယ့် အဆင့်" အတိုင်း လုပ်ပေး — Studio ကို ဒီ account မှာ publish လုပ်၊ backup data ထည့်၊ project.json ကို link အသစ်နဲ့ ပြင်ပြီး commit လုပ်ပေး။

6. **စမ်းကြည့်** — Claude ပို့တဲ့ Studio link ဖွင့် → `Dylan Blue` ရိုက်ရှာ → ပွင့်လာရမယ်။
   Chat မှာ ရေမွေးနာမည် တစ်ခု ရိုက် → ရှာပြီး Studio ထဲ ရောက်လာရမယ်။

## နည်း ၂ — claude.ai Project (chat သာမန်)

1. claude.ai → Projects → **New project** ("Perfume Review Studio")။
2. **Instructions** ထဲကို `PROJECT-INSTRUCTIONS.md` ရဲ့ `---` အောက်က စာ ကူးထည့်ပါ။
3. **Project knowledge** ထဲကို ဒီ file တွေ upload: `perfumes/*.md`၊ `studio/STUDIO-GUIDE.md`၊
   `.claude/skills/perfume-research/schema.md`၊ `.claude/skills/perfume-research/example.json`။
4. (ရရင်) Settings → Capabilities → Skills မှာ `perfume-research-skill.zip` ကို upload လုပ်ပါ။
5. Chat မှာ ရေမွေးနာမည် ရိုက်ရင် Claude က ရှာပြီး Studio ထဲ Import လုပ်လို့ရတဲ့ `.json` file
   ပေးပါလိမ့်မယ်။ ရေမွေး ၃ လုံးရဲ့ အချက်အလက်ကို မေးရင်လည်း `.md` file တွေကနေ ဖြေပါမယ်။

⚠️ Studio app ကိုယ်တိုင်က AI၊ database၊ web ရှာ capability တွေ လိုပါတယ်။ Chat သာမန်ကနေ ဒီလို
artifact ကို publish လုပ်လို့ ရမရ ကျွန်တော် မစစ်နိုင်ပါ — မရရင် Studio ကို နည်း ၁ နဲ့ တစ်ခါ
publish လုပ်ပြီး link ကို Project ထဲမှာ မှတ်ထားပါ။

## Data ကို ကိုယ်တိုင် ထည့်နည်း (Claude မလိုဘူး)

Studio ဖွင့် → အောက်က **Library** → အောက်ဆုံး **💾 Backup** → **⬆️ Import file ရွေးမယ်** →
`data/perfume-studio-backup.json` ရွေး → **"အသစ် ၃ ခု ထည့်မယ်"**။

## Claude လုပ်ရမယ့် အဆင့် (for Claude)

1. Load the `artifact-design` and `artifact-capabilities` skills, then publish
   `studio/perfume-research-studio.html` with the `Artifact` tool as a new artifact:
   `capabilities` = the object in `studio/capabilities.json`, `icon` = `perfume`,
   description "Burmese perfume research and review-script studio". The page has its own `<title>`.
2. Import the data: `python3 tools/split_backup.py data/perfume-studio-backup.json <scratchpad>/import`,
   then `ArtifactData` `set` each printed file (`collection` = `perfumes` or `vs`, `doc_id` = file
   name without `.json`, `file_path` = that file); batch at most 3 documents per call (they are large).
   Check with `ArtifactData` `list` that 3 perfumes are there.
3. Put the new link in `project.json` → `studio.url`, commit and push.
4. Optional: recreate the design canvas from `design/` (static mockup; not needed to run).
5. Send the user the Studio link in Burmese and remind them to keep Parallel Search connected.

## မပါနိုင်တာ

- ဒီ chat ရဲ့ စကားပြော မှတ်တမ်း၊ artifact version အဟောင်းတွေ — ဆုံးဖြတ်ချက် စည်းကမ်း အကုန်
  `CLAUDE.md` နဲ့ `PROJECT-INSTRUCTIONS.md` ထဲ ရေးထားလို့ အလုပ်လုပ်ပုံ မပြောင်းပါ။
- ရေမွေး ပုံတွေ (အခု data ထဲမှာ ပုံ မရှိပါ)။
- Data က export လုပ်တဲ့နေ့အထိပဲ — Studio ဟောင်းမှာ ထပ်ထည့်ရင် 💾 Export နဲ့ backup အသစ် ထုတ်ပါ။
