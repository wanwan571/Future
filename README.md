# ရေမွေး Review Studio

ရေမွေး review ဗီဒီယို ရိုက်ဖို့နဲ့ post တင်ဖို့ အချက်အလက်၊ script၊ ပြောစရာ၊ caption တွေကို
တစ်နေရာတည်းမှာ စုထားတဲ့ project ပါ။

## ဒီထဲမှာ ဘာတွေပါလဲ

| File | ဘာလဲ |
|---|---|
| `studio/perfume-research-studio.html` | Studio app (claude.ai artifact) |
| `studio/capabilities.json` | Studio သုံးခွင့်တွေ (AI၊ database၊ web ရှာ၊ download) |
| `data/perfume-studio-backup.json` | ရေမွေး data အကုန် (Dior Sauvage EDP၊ Versace Dylan Blue၊ YSL Y EDP) |
| `design/` | ဖုန်းအတွက် ဆွဲထားတဲ့ design canvas |
| `.claude/skills/perfume-research/` | Chat မှာ ရေမွေးနာမည် ရိုက်ရင် ရှာပြီး Studio ထဲ သိမ်းပေးမယ့် နည်းလမ်း |
| `CLAUDE.md` | Claude လိုက်နာရမယ့် စည်းကမ်းတွေ (English label၊ "မြန်မာ" မထည့်ရ စတာ) |
| `project.json` | Studio link၊ design link |
| `tools/split_backup.py` | Backup file ကို ရေမွေးတစ်လုံးချင်း ခွဲပေးတဲ့ tool (Claude သုံးဖို့) |

## နေ့စဉ် သုံးနည်း

1. **ရေမွေး ရှာမယ်** — Claude Code chat မှာ ရေမွေးနာမည် ရိုက်ပါ (ဥပမာ `Ramon Monegal Flamenco`)။
   Claude က web မှာ source တွေနဲ့ စစ်ပြီး Studio ထဲ အလိုလို သိမ်းပေးပါမယ်။ Brand နာမည်ချည်းပဲ
   ရိုက်ရင် ဘယ်ရေမွေးလဲ ပြန်မေးပါမယ်။
2. **Studio မှာ ဖွင့်မယ်** — နာမည်ရိုက်ရှာရင် သိမ်းထားတာကို ဖွင့်ပေးပါတယ်။ Chat က ရှာထားတဲ့
   ရေမွေးကို ပထမဆုံး ဖွင့်တဲ့အခါ script၊ ပြောစရာ၊ Post၊ Hook တွေကို အဲဒီ အချက်တွေပေါ်ကပဲ
   အလိုလို ရေးပေးပါတယ်။ 🔬 အမှတ်အသားက "Chat က source နဲ့ စစ်ပြီး" လို့ ဆိုလိုပါတယ်။
3. **စစ်ပြီးသား အချက်တွေ ကာကွယ်ထားတယ်** — Chat က စစ်ထားတဲ့ အချက်တွေကို AI က အလိုလို
   မပြင်ပါဘူး။ ကွက်လပ်တွေပဲ ဖြည့်ပြီး မတူတာ တွေ့ရင် ⚠️ နဲ့ ပြပါတယ်။
4. **Queue** — Studio မှာ "Web နဲ့ စစ်ခိုင်းမယ်" နှိပ်ထားတဲ့ ရေမွေးတွေကို chat မှာ
   `Studio queue ထဲက ရှာပေး` လို့ ပြောရင် အကုန် ရှာပေးပါတယ်။
5. **Backup** — Studio → Library → 💾 Backup → ⬇️ Export နဲ့ data အကုန်ကို file တစ်ခုထဲ
   အချိန်မရွေး သိမ်းလို့ရပါတယ်။

## တခြား account ထဲ ပြန်ထည့်နည်း

Account ဟောင်းထဲက ဘာမှ မပျက်ပါဘူး — account အသစ်မှာ မိတ္တူ တစ်ခု ထပ်တည်တာပါ။

### ၁။ Account အသစ်မှာ ပြင်ဆင်ရန်

- claude.ai → Settings → Connectors → **Parallel Search** ကို ချိတ်ပါ
  (Studio ထဲက web ရှာတာနဲ့ chat က ရေမွေးရှာတာ နှစ်ခုလုံး ဒါကို သုံးပါတယ်)။
- claude.ai/code ကို ဖွင့်ပြီး GitHub ချိတ်ပါ။

### ၂။ File တွေ ယူရန် (တစ်နည်းနည်း)

- **GitHub နည်း** — ဒီ repo (`saikhaywunnukone-blip/future`) ကို account အသစ်ရဲ့ Claude Code
  session မှာ ဖွင့်ပါ။ GitHub account မတူရင် ဒီ repo ကို fork လုပ်ပါ၊ ဒါမှမဟုတ် zip ထဲက
  file တွေကို repo အသစ်ထဲ တင်ပါ။
- **Zip နည်း** — `perfume-studio-export.zip` ကို ဖြည်ပြီး repo အသစ်ထဲ တင်ပါ။

### ၃။ Claude ကို ဒီစာ ပို့ပါ

> README ထဲက "တခြား account ထဲ ပြန်ထည့်နည်း" အတိုင်း လုပ်ပေး — Studio ကို ဒီ account မှာ publish လုပ်၊ backup data ထည့်၊ project.json ကို link အသစ်နဲ့ ပြင်ပေး။

Claude လုပ်ရမယ့် အဆင့်တွေ (for Claude):

1. `studio/perfume-research-studio.html` ကို `Artifact` tool နဲ့ artifact အသစ်အဖြစ် publish:
   `capabilities` = `studio/capabilities.json` ထဲက object၊ `icon` = `perfume`၊ title =
   "ရေမွေး Review Studio" (page ထဲမှာ `<title>` ပါပြီးသား)။ Load the `artifact-design` and
   `artifact-capabilities` skills first, as the Artifact tool requires.
2. Data ထည့်: `python3 tools/split_backup.py data/perfume-studio-backup.json <scratchpad>/import`
   ပြီးရင် ထွက်လာတဲ့ file တစ်ခုစီကို `ArtifactData` `set` (collection = `perfumes` သို့ `vs`၊
   `doc_id` = file နာမည်၊ `file_path` = အဲဒီ file) — document တွေ ကြီးလို့ batch တစ်ခုမှာ ၃ ခုစီ။
3. `project.json` ထဲက `studio.url` ကို link အသစ်နဲ့ ပြင်ပြီး commit လုပ်။
4. (မဖြစ်မနေ မဟုတ်) `design/` ထဲက file တွေနဲ့ design canvas ကို ပြန်တည်။
5. Studio link ကို user ကို ပို့ပြီး Parallel Search ချိတ်ထားဖို့ သတိပေး။

**Claude မသုံးဘဲ data ထည့်ချင်ရင်:** Studio အသစ်ကို ဖွင့် → Library → 💾 Backup →
⬆️ Import file ရွေးမယ် → `perfume-studio-backup.json` ရွေး → "အသစ် … ခု ထည့်မယ်"။

### ၄။ စမ်းကြည့်ရန်

- Studio မှာ `Dylan Blue` ရိုက်ရှာ → သိမ်းထားတာ ပွင့်လာရမယ်။
- Chat မှာ ရေမွေးနာမည် တစ်ခု ရိုက် → ရှာပြီး Studio ထဲ ရောက်လာရမယ်။

### မပါနိုင်တာ

- ဒီ chat ရဲ့ စကားပြော မှတ်တမ်းနဲ့ artifact ရဲ့ version အဟောင်းတွေ (စည်းကမ်း၊ ဆုံးဖြတ်ချက်
  အကုန်ကို `CLAUDE.md` ထဲ ရေးထားလို့ အလုပ်လုပ်ပုံ မပြောင်းပါဘူး)။
- ရေမွေး ပုံတွေ (အခု data ထဲမှာ ပုံ မရှိပါ)။
