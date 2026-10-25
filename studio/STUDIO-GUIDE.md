# Studio guide — ဘာတွေလုပ်လို့ရလဲ၊ ဘယ်လို တည်ဆောက်ထားလဲ

`perfume-research-studio.html` က claude.ai artifact (HTML page တစ်ခုတည်း) ပါ။ Library တစ်ခုမှ
မလိုဘဲ JavaScript နဲ့ ရေးထားပြီး ဖုန်းနဲ့ သုံးဖို့ ဒီဇိုင်းလုပ်ထားပါတယ်။

## သုံးသူအတွက် — ခလုတ်တွေ

**Home**
- ရေမွေးနာမည် ရိုက်ရှာ → Library ထဲမှာ ရှိပြီးသားဆို ဖွင့်ပေး၊ မရှိရင် 🌐 Web (Parallel Search)
  နဲ့ ရှာပြီး သိမ်း။ "အချက်အလက်ပဲ အရင်ရှာ" ကို ✓ ထားရင် script တွေ ချက်ချင်း မထုတ်ဘဲ
  အချက်အလက် စစ်ပြီးမှ ထုတ်ခိုင်းရ။
- "နောက်တစ်ဆင့်" — ရေမွေးတစ်လုံးချင်း ဘာလုပ်ရဦးမလဲ ပြ။

**Library** (အောက်က nav)
- Filter (ရာသီ၊ ရုံး၊ ညပွဲ၊ Men / Women / Unisex၊ ✅ Web — Chat က ရှာထားတာပါ ပါ၊ 🔀 Source စစ်ပြီး၊
  ⚠️ AI draft)၊ နာမည်/note ရှာ။
- ⚖️ VS — ၂–၃ လုံး ရွေးပြီး နှိုင်းယှဉ် Reel script။
- 🗑️ ရွေးပြီး ဖျက် / 📦 Archive (ပြန်ထုတ်၊ ဖျက်)။
- 📚 Note အဘိဓာန် — ရေမွေးအားလုံးထဲက note တွေ။
- 💾 Backup — ⬇️ Export (data အကုန် .json file တစ်ခု) / ⬆️ Import (backup file ပြန်ထည့်)။

**ရေမွေး စာမျက်နှာ** — အောက်က tab ၅ ခု
- **အချက်** — အကျဉ်း၊ Accords၊ Performance (Longevity၊ Projection၊ Sweetness၊ Day/Night၊
  Masculine/Feminine)၊ ရာသီ၊ Notes Pyramid၊ အနံ့ ပြောင်းပုံ၊ အသေးစိတ် ဇာတ်လမ်း ၁၂ ပိုင်း၊
  ရိုက်ဖို့ အဆင်သင့်ဖြစ်ပြီလား checklist။
- **စစ်ဆေး** — 🌐 Web နဲ့ ပြန်စစ်၊ ကိုယ်ရှာထားတဲ့ စာ/screenshot ထည့်ပြီး AI နဲ့ ပေါင်းစစ်
  (ပြောင်းမယ့်အချက်ကို ကိုယ်တိုင် ရွေးမှ သုံး)၊ နှိုင်းယှဉ်ချက်၊ အစစ်/အတု၊ FAQ၊ Sources၊
  📄 PDF / Export၊ ဝတ်စမ်းရန် checklist။
- **Script** — ဗီဒီယိုရှည် (scene ၁၀)၊ Reel ၆၀ စက္ကန့်၊ ကိုယ်တိုင်စမ်းချက် (Longevity နာရီ၊ ဈေး —
  script ထဲ အလိုလို ဝင်)။
- **ပြောစရာ** — အသံထွက်၊ ပြောလို့ရတဲ့ အချက်၊ မပြောသင့်တာ၊ အနံ့ ပြောနည်း၊ ဝတ်နည်း၊ Hook ၁၀ မျိုး၊
  Content idea။
- **Post** — Caption + ပြန်စာ (ကူးသုံးရန်)။
- အပေါ်ဘား: ▶ ရိုက်မယ် (teleprompter)၊ 📄 PDF (အချက်အလက် အကုန် PDF ကြည့်/download)၊ ⋯ စီမံရန်
  (အခြေအနေ၊ Archive၊ ဖျက်၊ ပြန်ရှာ)။

**🔬 Chat က ရှာထားတဲ့ ရေမွေး** (`researchedBy: "chat"`)
- ပထမဆုံး ဖွင့်တာနဲ့ မရှိသေးတဲ့ script၊ ပြောစရာ၊ Post၊ Hook တွေကို အလိုလို ရေး။
- "အကုန် ပြန်ရေးမယ်" — script တွေပဲ ပြန်ရေး၊ ရှာထားတဲ့ အသေးစိတ်/နှိုင်းယှဉ်/FAQ မထိ။
- 🌐 Web နဲ့ ပြန်စစ် — ကွက်လပ်တွေပဲ ဖြည့်၊ source အသစ် ထပ်ထည့်။
- ကိုယ်ရှာထားတဲ့ info ပေါင်းစစ် — ဘာမှ အလိုလို မရွေး။

## Developer အတွက်

**Capabilities** (`capabilities.json`) — `sample` (Claude AI၊ ပုံ ပါ)၊ `db` (database)၊ `user`၊
`assets` (ပုံ)၊ `downloads` (PDF / backup file)၊ `mcp` → Parallel Search `web_search`။
Page က `window.claude.use(name)` နဲ့ ယူသုံး။ မရတဲ့ capability ရှိရင် အဲဒီ feature ပဲ ပိတ်သွား။

**Database**
- `perfumes/<id>` — ရေမွေး တစ်လုံး document တစ်ခု။ Field တွေက
  `../.claude/skills/perfume-research/schema.md` အတိုင်း + Studio ထုတ်တဲ့ အပိုင်းတွေ:
  `script`, `shoot`, `captions`, `selftest`, `images` (content)၊ `longscript` (scene ၁၀)၊
  `talk` (pronounce / facts / avoid / smell_words / wear_tips)၊ `hooks`, `angles` (ideas)၊
  `test` (ကိုယ်တိုင်စမ်းချက်)၊ `price`, `status`, `archived`, `photo`, `inputs` (ထည့်ထားတဲ့ source)၊
  `reconcile` (ပေါင်းစစ်ချက် စောင့်နေတာ)၊ `mergeLog`, `staleAt`, `verifyRequest`။
- `vs/<idA__idB>` — သိမ်းထားတဲ့ VS script။
- Document id = နာမည်ရဲ့ slug (`Dior Sauvage Eau de Parfum` → `dior-sauvage-eau-de-parfum`)။

**AI ခေါ်ပုံ** — prompt တွေ အကုန် page ထဲမှာ (`BASE`, `factsPrompt`, `webFactsPrompt`,
`deepPrompt`, `extraPrompt`, `contentPrompt`, `longPrompt`, `talkPrompt`, `ideasPrompt`,
`mergePrompt`, `vsPrompt`)။ Script ရေးတဲ့ prompt တွေက `factSummary(v)` + `GROUND` စည်းကမ်းနဲ့
သိမ်းထားတဲ့ အချက်တွေကိုပဲ အခြေခံ။ `BASE` ထဲမှာ ဘာသာစကား စည်းကမ်း (Burmese စာ၊ English
နာမည်/term၊ "မြန်မာ" qualifier မသုံး) ပါ။

**Web ရှာပုံ** — `web_search` ၂ ကြိမ် → result စာ (≤42k) → `webFactsPrompt` → `normFacts`။ Result ထဲ
တကယ်ပါတဲ့ URL ကိုပဲ source အဖြစ် လက်ခံ။

**PDF** — `docPaper` က block တွေ ဆောက်၊ html2canvas နဲ့ ပုံဆွဲ၊ jsPDF နဲ့ A4 စာမျက်နှာ စီ
(မြန်မာစာ မှန်အောင် ပုံအဖြစ်)။ ခေါင်းစဉ်က နောက်က စာနဲ့ တွဲ၊ စာရှည်ကို စာကြောင်းကြား
အဖြူကွက်မှာ ဖြတ်။ Library ကို cdnjs ကနေ load။

**Code ပုံစံ** — `h(tag, props, ...kids)` DOM builder၊ state အကုန် `S` ထဲ၊ `render()` က screen
တစ်ခုလုံး ပြန်ဆွဲ (input ကို ရိုက်နေတုန်း မဆွဲ)၊ ရေးတာက `patchDoc(id, patch)` / `setDoc(id, doc)`။

**ပြင်ပြီး publish** — HTML ကို ပြင် → headless Chromium မှာ `window.claude.use` ကို mock လုပ်ပြီး
စမ်း → `Artifact` tool နဲ့ `project.json` ထဲက `studio.url` ကို publish (ပထမဆုံး account အသစ်မှာဆို
`capabilities` ကို `capabilities.json` အတိုင်း ပေး၊ နောက်ပိုင်း ချန်ထားရင် အဟောင်းအတိုင်း)။
