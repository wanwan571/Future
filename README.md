# ရေမွေး Review Studio

ရေမွေး review ဗီဒီယို ရိုက်ဖို့နဲ့ post တင်ဖို့ အချက်အလက်၊ script၊ ပြောစရာ၊ caption တွေကို
တစ်နေရာတည်းမှာ စုထားတဲ့ project ပါ။

**Account အသစ်မှာ ပြန်တည်ချင်ရင် → [`START-HERE.md`](START-HERE.md)**

## ဒီထဲမှာ ဘာတွေပါလဲ

| File | ဘာလဲ |
|---|---|
| `START-HERE.md` | Account အသစ်မှာ ပြန်တည်နည်း (အဆင့်လိုက်) |
| `studio/perfume-research-studio.html` | Studio app code (claude.ai artifact) |
| `studio/capabilities.json` | Studio သုံးခွင့်တွေ (AI၊ database၊ web ရှာ၊ download) |
| `studio/STUDIO-GUIDE.md` | Studio ခလုတ်တွေ၊ data ပုံစံ၊ AI prompt တွေ ရှင်းပြချက် |
| `data/perfume-studio-backup.json` | ရေမွေး data အကုန် (Studio ထဲ Import လုပ်ဖို့) |
| `data/perfumes/*.json` | ရေမွေး တစ်လုံးချင်း backup |
| `perfumes/*.md` | ရေမွေး တစ်လုံးချင်း အချက်အလက်၊ script၊ caption အကုန် — ဖတ်ဖို့ |
| `design/` | ဖုန်းအတွက် ဆွဲထားတဲ့ design canvas |
| `.claude/skills/perfume-research/` | Chat မှာ ရေမွေးနာမည် ရိုက်ရင် ရှာပြီး Studio ထဲ သိမ်းတဲ့ skill (schema၊ ဥပမာ၊ စစ်တဲ့ script) |
| `CLAUDE.md` | Claude Code လိုက်နာရမယ့် စည်းကမ်း (English label၊ "မြန်မာ" မထည့်ရ စတာ) |
| `PROJECT-INSTRUCTIONS.md` | claude.ai Project ရဲ့ Instructions ထဲ ကူးထည့်ဖို့ |
| `project.json` | Studio link၊ design link |
| `tools/split_backup.py` | Backup ကို ရေမွေးတစ်လုံးချင်း ခွဲ (Claude က database ထဲ ထည့်ဖို့) |
| `tools/make_markdown.py` | Backup ကနေ `perfumes/*.md` ပြန်ထုတ် |

## နေ့စဉ် သုံးနည်း

1. **ရေမွေး ရှာမယ်** — Claude chat မှာ ရေမွေးနာမည် ရိုက်ပါ (ဥပမာ `Ramon Monegal Flamenco`)။
   Claude က web မှာ source တွေနဲ့ စစ်ပြီး Studio ထဲ သိမ်းပေးပါမယ်။ Brand နာမည်ချည်းပဲ
   ရိုက်ရင် ဘယ်ရေမွေးလဲ ပြန်မေးပါမယ်။
2. **Studio မှာ ဖွင့်မယ်** — နာမည်ရိုက်ရှာရင် သိမ်းထားတာကို ဖွင့်ပေးပါတယ်။ Chat က ရှာထားတဲ့
   ရေမွေး (🔬) ကို ပထမဆုံး ဖွင့်တဲ့အခါ script၊ ပြောစရာ၊ Post၊ Hook တွေကို အဲဒီ အချက်တွေပေါ်ကပဲ
   အလိုလို ရေးပေးပါတယ်။
3. **စစ်ပြီးသား အချက်တွေ ကာကွယ်ထားတယ်** — Chat က စစ်ထားတဲ့ အချက်တွေကို AI က အလိုလို
   မပြင်ပါဘူး။ ကွက်လပ်တွေပဲ ဖြည့်ပြီး မတူတာ တွေ့ရင် ⚠️ နဲ့ ပြပါတယ်။
4. **Queue** — Studio မှာ "Web နဲ့ စစ်ခိုင်းမယ်" နှိပ်ထားတဲ့ ရေမွေးတွေကို chat မှာ
   `Studio queue ထဲက ရှာပေး` လို့ ပြောရင် အကုန် ရှာပေးပါတယ်။
5. **Backup** — Studio → Library → 💾 Backup → ⬇️ Export နဲ့ data အကုန်ကို file တစ်ခုထဲ
   အချိန်မရွေး သိမ်းလို့ရပါတယ်။
