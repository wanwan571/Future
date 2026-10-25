"""Write one readable Markdown file per perfume from a Studio backup.

usage: python3 tools/make_markdown.py data/perfume-studio-backup.json perfumes/
Every field the Studio stores is included: facts, deep dive, comparison, FAQ, talking points,
scripts, captions, ideas, shoot prep and sources.
"""
import json
import os
import sys
from datetime import datetime, timezone

DEEP_TITLES = {
    "history": "ထွက်ရှိမှုနဲ့ ဇာတ်လမ်း", "perfumer": "ဖန်တီးသူ", "design": "ပုလင်းနဲ့ ထုပ်ပိုးမှု",
    "campaign": "ကြော်ငြာနဲ့ မျက်နှာ", "name": "နာမည်ရဲ့ အဓိပ္ပါယ်", "notes_detail": "Note တစ်ခုချင်း အသေးစိတ်",
    "journey": "အနံ့ခရီး မိနစ်အလိုက်", "performance": "Longevity & Projection", "audience": "ဘယ်သူ ဘယ်အချိန်",
    "community": "Community အမြင်", "versions": "Line ထဲက version တွေ", "buying": "ဝယ်ယူမှု အကြံပြုချက်",
}
DEEP_ORDER = list(DEEP_TITLES)
KIND = {"history": "📅 သမိုင်း", "perfumer": "👤 ဖန်တီးသူ", "ingredient": "🧪 ပါဝင်ပစ္စည်း", "bottle": "🍾 ပုလင်း",
        "campaign": "📢 ကြော်ငြာ", "performance": "⏱️ Performance", "trivia": "💡 စိတ်ဝင်စားစရာ"}


def cell(x):
    return str(x if x is not None else "").replace("|", "\\|").replace("\n", "<br>").strip() or "—"


def table(heads, rows):
    if not rows:
        return []
    out = ["| " + " | ".join(heads) + " |", "|" + "---|" * len(heads)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return out + [""]


def ul(items):
    return [f"- {str(i).strip()}" for i in items if str(i).strip()] + ([""] if items else [])


def dots(n):
    try:
        n = max(0, min(5, round(float(n))))
    except (TypeError, ValueError):
        return ""
    return "●" * n + "○" * (5 - n)


def ymd(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%d") if ms else ""


def mmss(s):
    s = int(s or 0)
    return f"{s // 60}:{s % 60:02d}"


def stage_of(n):
    s = str(n.get("stage", "")).strip().split(" ")[0].split("(")[0].lower()
    return {"top": "Top", "heart": "Heart", "middle": "Heart", "base": "Base"}.get(s, "Other")


def verified(d):
    n = len(d.get("sources") or [])
    if d.get("researchedBy") == "chat":
        return f"🔬 Chat က source {n} ခုနဲ့ အသေးစိတ် စစ်ပြီး · {ymd(d.get('verifiedAt'))}"
    if d.get("origin") == "web":
        return f"✅ Web နဲ့ စစ်ပြီး · {ymd(d.get('verifiedAt'))}"
    if d.get("origin") == "merged":
        return f"🔀 Source {d.get('mergedN', '')} ခုနဲ့ စစ်ထုတ်ပြီး"
    return "⚠️ AI draft — web မစစ်ရသေး"


def render(d):
    L = [f"# {d.get('name')}", "", f"> {verified(d)}", ""]
    if d.get("one_liner"):
        L += [f"**{d['one_liner']}**", ""]
    if d.get("verdict"):
        L += [d["verdict"], ""]

    L += ["## အခြေခံ အချက်အလက်", ""]
    L += table(["", ""], [[k, v] for k, v in [
        ("Brand", d.get("brand")), ("Concentration", d.get("concentration")), ("ထွက်တဲ့နှစ်", d.get("year")),
        ("Perfumer", d.get("perfumer")), ("Family", d.get("family")), ("Gender", d.get("gender")),
        ("Size", d.get("sizes")), ("ပုလင်း", d.get("bottle")), ("ရည်ညွှန်းဈေး", d.get("ref_price")),
        ("ဘယ်သူနဲ့ ကိုက်", d.get("target")), ("တခြား version", " · ".join(d.get("alternatives") or [])),
    ] if str(v or "").strip()])

    m = d.get("meters") or {}
    L += ["## Accords & Performance", ""]
    L += [f"- **{a['name'].title()}** — {a.get('pct')}%" for a in d.get("accords") or []] + [""]
    perf = [("Longevity", f"{dots(m.get('longevity'))} {d.get('longevity_text', '')}"),
            ("Projection", f"{dots(m.get('projection'))} {d.get('projection_text', '')}"),
            ("Sweetness", dots(m.get("sweetness"))),
            ("Day / Night", f"Day {m['day']}% · Night {100 - m['day']}%" if m.get("day") is not None else ""),
            ("Masculine / Feminine", f"{m['masculine']}% / {100 - m['masculine']}%" if m.get("masculine") is not None else ""),
            ("ရာသီဥတု", d.get("myanmar_tip"))]
    L += table(["", ""], [[k, v] for k, v in perf if str(v or "").strip()])

    notes = d.get("notes") or []
    if notes:
        L += ["## Notes Pyramid", ""]
        for st in ("Top", "Heart", "Base", "Other"):
            ns = [n for n in notes if stage_of(n) == st]
            if ns:
                L += [f"### {st} Notes" if st != "Other" else "### အခြား", ""]
                L += [f"- **{n['note']}** — {n.get('smell', '')}{' ⚠ source ကွဲ' if n.get('certain') is False else ''}" for n in ns] + [""]
    if d.get("phases"):
        L += ["### ဖျန်းပြီးနောက် အနံ့ ပြောင်းပုံ", ""]
        for p in d["phases"]:
            stage = str(p.get("stage", "")).split(" (")[0]
            L.append(f"- **{stage}** · {p.get('time_text') or str(p.get('start_h')) + '–' + str(p.get('end_h')) + ' နာရီ'} — {p.get('summary', '')}"
                     + (f" ({p['feel']})" if p.get("feel") else "") + (f" · {p['analogy']}" if p.get("analogy") else ""))
        L.append("")

    if d.get("seasons") or d.get("occasions"):
        L += ["## ဘယ်အချိန် ဝတ်မလဲ", ""]
        L += table(["ရာသီ", "ကိုက်ညီမှု", "ဖျန်းနည်း", "အကြံပြုချက်"],
                   [[f"{s.get('season')} ({s.get('months', '')})", f"{dots(s.get('fit'))} {s.get('fit')}/5", s.get("sprays"), s.get("advice")] for s in d.get("seasons") or []])
        L += table(["အခါသမယ", "ကိုက်ညီမှု", "ဘာကြောင့်"],
                   [[o.get("occasion"), f"{dots(o.get('fit'))} {o.get('fit')}/5", o.get("note")] for o in d.get("occasions") or []])
    if d.get("pros") or d.get("cons"):
        L += ["## ကောင်းကွက် / အားနည်းကွက်", "", "**👍 ကောင်းကွက်**", ""] + ul(d.get("pros") or []) + ["**👎 အားနည်းကွက်**", ""] + ul(d.get("cons") or [])
    if d.get("concept") or d.get("concept_title") or d.get("hook"):
        L += ["## Brand ရဲ့ ဇာတ်လမ်း", ""]
        if d.get("concept_title"):
            L += [f"### {d['concept_title']}", ""]
        if d.get("concept"):
            L += [d["concept"], ""]
        if d.get("hook"):
            L += [f"**Hook idea:** {d['hook']}", ""]

    deep = {s.get("key"): s for s in d.get("deep") or []}
    if deep:
        L += ["## အသေးစိတ် ဇာတ်လမ်း", ""]
        for k in DEEP_ORDER + [k for k in deep if k not in DEEP_ORDER]:
            s = deep.get(k)
            if not s:
                continue
            L += [f"### {DEEP_TITLES.get(k, s.get('title') or k)}", ""]
            L += [p.strip() + "\n" for p in str(s.get("body", "")).split("\n\n") if p.strip()]
            L += ul(s.get("bullets") or [])

    if d.get("compare"):
        L += ["## နှိုင်းယှဉ်ချက်", ""]
        L += table(["ရေမွေး", "အုပ်စု", "နှစ်", "ဘာကွာလဲ", "Fresh", "Sweet", "Strength", "Longevity", "အကောင်းဆုံး"],
                   [[c.get("name", "") + (" ★" if c.get("is_self") else ""), c.get("group"), c.get("year"), c.get("character"),
                     c.get("fresh"), c.get("sweet"), c.get("strength"), c.get("longevity"), c.get("best_for")] for c in d["compare"]])
    if d.get("authenticity"):
        L += ["## အစစ် / အတု ခွဲနည်း", ""]
        L += table(["စစ်ရမယ့်နေရာ", "အစစ်", "သံသယ"], [[a.get("area"), a.get("check"), a.get("red_flag")] for a in d["authenticity"]])
    if d.get("faq"):
        L += ["## Customer မေးလေ့ရှိတဲ့ မေးခွန်း", ""]
        for f in d["faq"]:
            L += [f"**Q · {f.get('q')}**", "", f.get("a", ""), ""]

    T = d.get("talk") or {}
    if any(T.get(k) for k in ("pronounce", "facts", "avoid", "smell_words", "wear_tips")):
        L += ["## ကင်မရာရှေ့ ပြောစရာ", ""]
        if T.get("pronounce"):
            L += ["### 🗣️ အသံထွက်", ""] + table(["စာလုံး", "အသံထွက်", "မှတ်ချက်"], [[p.get("term"), p.get("say"), p.get("tip")] for p in T["pronounce"]])
        if T.get("facts"):
            L += ["### ✅ ပြောလို့ရတဲ့ အချက်", ""]
            L += [f"- {'✅' if f.get('sure') else '⚠ စစ်ရန် ·'} {KIND.get(f.get('kind'), '')} {f.get('fact', '')}" + (f" — “{f['say']}”" if f.get("say") else "") for f in T["facts"]] + [""]
        if T.get("avoid"):
            L += ["### 🚫 မပြောသင့်တာ", ""] + table(["မပြောရ", "ဘာကြောင့် · အစား ဘာပြော"], [[a.get("claim"), a.get("why")] for a in T["avoid"]])
        if T.get("smell_words"):
            L += ["### 👃 အနံ့ ပြောနည်း", ""]
            L += [f"- **{s.get('stage')}:** {'၊ '.join(s.get('words') or [])}" + (f" · {s['compare']}" if s.get("compare") else "") + (f" — “{s['say']}”" if s.get("say") else "") for s in T["smell_words"]] + [""]
        if T.get("wear_tips"):
            L += ["### 💡 ဝတ်နည်း / သိမ်းနည်း", ""] + [f"- **{w.get('tip')}:** {w.get('detail', '')}" for w in T["wear_tips"]] + [""]

    scenes = (d.get("longscript") or {}).get("scenes") or []
    if scenes or d.get("script"):
        L += ["## Video Script", ""]
        if scenes:
            ls = d["longscript"]
            L += [f"*{ls.get('platform', '')}{' · ' + ls['format'] if ls.get('format') else ''}*", ""]
        for i, s in enumerate(scenes, 1):
            L += [f"### SCENE {i} · {s.get('title', '')} ({mmss(s.get('start_s'))}–{mmss(s.get('end_s'))})", ""]
            if s.get("shots"):
                L += [f"*[ရိုက်ကွက်]* {' · '.join(s['shots'])}", ""]
            for sub in s.get("subsections") or []:
                if sub.get("title"):
                    L += [f"**{sub['title']}**", ""]
                L += [str(x) + "\n" for x in sub.get("lines") or []]
            L += [str(x) + "\n" for x in s.get("lines") or []]
            if s.get("rating"):
                L += [f"- {r.get('label')}: {'★' * int(r.get('stars') or 0)}" for r in s["rating"]] + [""]
            if s.get("screen"):
                L += [f"*[Screen]* {' · '.join(str(x) for x in s['screen'])}", ""]
            if s.get("broll"):
                L += [f"*[B-roll]* {' · '.join(str(x) for x in s['broll'])}", ""]
            if s.get("note"):
                L += [f"*မှတ်ချက်:* {s['note']}", ""]
        if d.get("script"):
            L += ["### Reel / TikTok — ၆၀ စက္ကန့်", ""]
            L += table(["အချိန်", "ပြောမယ့်စာ", "ရိုက်မယ့်ပုံ", "Screen"],
                       [[f"{r.get('start_s')}–{r.get('end_s')}s · {r.get('part', '')}", r.get("say"), r.get("shot"), r.get("screen")] for r in d["script"]])
    if d.get("captions"):
        L += ["## Caption / Post", ""]
        for c in d["captions"]:
            L += [f"### {c.get('channel', '')} — {c.get('purpose', '')}", "", "```", str(c.get("text", "")).strip(), "```", ""]
    if d.get("hooks") or d.get("angles"):
        L += ["## Hook နဲ့ Content idea", ""]
        L += table(["အမျိုးအစား", "Hook", "Screen စာ"], [[h.get("type"), h.get("text"), h.get("screen")] for h in d.get("hooks") or []])
        L += table(["Idea", "Format", "ဘာပြမလဲ", "ဘာကြောင့်"], [[a.get("title"), a.get("format"), a.get("idea"), a.get("why")] for a in d.get("angles") or []])
    if d.get("shoot") or d.get("images") or d.get("selftest"):
        L += ["## ရိုက်ကူးရေး ပြင်ဆင်ရန်", ""]
        L += table(["အုပ်စု", "အရာ", "အသေးစိတ်"], [[s.get("group"), s.get("item"), s.get("detail")] for s in d.get("shoot") or []])
        im = d.get("images") or {}
        L += table(["ပုံ", "Idea"], [[k, im[k]] for k in ("thumbnail", "concept", "flatlay", "colors") if im.get(k)])
        L += table(["ဘယ်အချိန်", "စစ်ရမှာ", "မှတ်ရမှာ"], [[s.get("when"), s.get("check"), s.get("record")] for s in d.get("selftest") or []])
    t = {k: v for k, v in (d.get("test") or {}).items() if str(v).strip() and k != "done"}
    if t or str(d.get("price") or "").strip():
        L += ["## ကိုယ်တိုင် စမ်းထားချက်", ""] + table(["", ""], [[k, v] for k, v in t.items()] + ([["ဆိုင်ဈေး", d["price"]]] if d.get("price") else []))
    if d.get("uncertain") or d.get("verify"):
        L += ["## မသေချာတဲ့ အချက် / ဆက်စစ်ရန်", ""] + ul(d.get("uncertain") or []) + ul(d.get("verify") or [])
    if d.get("sources"):
        L += ["## Sources", ""] + [f"- [{s.get('label')}]({s.get('url')}) — {s.get('topic', '')}" for s in d["sources"]] + [""]
    L += ["---", "", "*`{HOURS}`, `{PRICE_FULL}`, `{PRICE_10ML}`, `{PRICE_5ML}` — Studio ရဲ့ ကိုယ်တိုင်စမ်း tab မှာ ဖြည့်ရင် အလိုလို အစားထိုးတဲ့ နေရာတွေပါ။*", ""]
    return "\n".join(L)


if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    bk = json.load(open(src, encoding="utf-8"))
    os.makedirs(out, exist_ok=True)
    for d in bk["perfumes"]:
        path = os.path.join(out, d["id"] + ".md")
        open(path, "w", encoding="utf-8").write(render(d))
        print(path)
