"""Check a Studio perfume document before saving it.

usage: python3 validate.py doc.json
Exits 1 and lists the problems if the document breaks the schema or the language rules.
"""
import json
import re
import sys

DEEP = ["history", "perfumer", "design", "campaign", "name", "notes_detail",
        "journey", "performance", "audience", "community", "versions", "buying"]
STRINGS = ["name", "title", "brand", "concentration", "year", "perfumer", "family", "gender", "sizes",
           "bottle", "longevity_text", "projection_text", "ref_price", "concept_title", "concept",
           "one_liner", "verdict", "target", "myanmar_tip", "hook", "query"]
LISTS = ["alternatives", "accords", "phases", "notes", "seasons", "occasions", "pros", "cons",
         "uncertain", "verify", "deep", "compare", "authenticity", "faq", "sources"]
# words the seller asked to keep out: Burmese perfume terms (use English) and "Myanmar" as a qualifier
BANNED = {"မြန်မာ ": "write no 'မြန်မာ' qualifier", "မြန်မာနိုင်ငံ": "write no 'မြန်မာနိုင်ငံ' qualifier",
          "Myanmar": "write no 'Myanmar' qualifier", "ခံချိန်": "use 'Longevity'", "ခံနိုင်ရည်": "use 'Longevity'",
          "ပျံ့နှံ့": "use 'Projection'"}
BURMESE = re.compile(r"[က-႟]")


def problems(d):
    out = []
    need = lambda c, msg: c or out.append(msg)
    need(d.get("v") == 2, 'v must be 2')
    need(d.get("origin") == "web", 'origin must be "web"')
    need(d.get("researchedBy") == "chat", 'researchedBy must be "chat"')
    for k in ("createdAt", "updatedAt", "verifiedAt", "webAt"):
        need(isinstance(d.get(k), int) and d[k] > 1_600_000_000_000, f"{k} must be epoch milliseconds")
    need(isinstance(d.get("test"), dict), "test must be an object")
    for k in STRINGS:
        need(isinstance(d.get(k), str) and d[k].strip(), f"{k} must be a non-empty string")
    for k in LISTS:
        need(isinstance(d.get(k), list) and d[k], f"{k} must be a non-empty list")
    if out:
        return out
    need(d["title"] == d["name"], "title must equal name")
    for a in d["accords"]:
        need(a.get("name") == str(a.get("name", "")).lower() and not BURMESE.search(a["name"]), f"accord name must be lowercase English: {a}")
        need(isinstance(a.get("pct"), int) and 5 <= a["pct"] <= 100, f"accord pct 5–100: {a}")
    m = d.get("meters", {})
    for k in ("longevity", "projection", "sweetness"):
        need(isinstance(m.get(k), int) and 1 <= m[k] <= 5, f"meters.{k} must be 1–5")
    for k in ("day", "masculine"):
        need(isinstance(m.get(k), int) and 0 <= m[k] <= 100, f"meters.{k} must be 0–100")
    need([p.get("stage") for p in d["phases"]] == ["Top", "Heart", "Base"], 'phases stages must be "Top", "Heart", "Base"')
    for n in d["notes"]:
        need(n.get("stage") in ("Top", "Heart", "Base"), f"note stage: {n.get('note')}")
        need(n.get("note") and not BURMESE.search(n["note"]), f"note name must be English only: {n.get('note')}")
        need(isinstance(n.get("certain"), bool), f"note certain must be true/false: {n.get('note')}")
    need([s.get("season") for s in d["seasons"]] == ["နွေ", "မိုး", "ဆောင်း"], "seasons must be နွေ, မိုး, ဆောင်း")
    for s in d["seasons"] + d["occasions"]:
        need(isinstance(s.get("fit"), int) and 1 <= s["fit"] <= 5, f"fit 1–5: {s}")
    need([x.get("key") for x in d["deep"]] == DEEP, "deep must have the 12 keys in order: " + ", ".join(DEEP))
    listed = ("notes_detail", "journey", "versions")  # a short intro, the detail is in the bullets
    for x in d["deep"]:
        need(isinstance(x.get("body"), str) and len(x["body"]) > (20 if x.get("key") in listed else 300), f"deep {x.get('key')}: body too short")
        need(isinstance(x.get("bullets"), list), f"deep {x.get('key')}: bullets must be a list")
    for k in listed:
        sec = next((x for x in d["deep"] if x.get("key") == k), {})
        need(len(sec.get("bullets", [])) >= 3, f"deep {k}: needs bullets")
    need(5 <= len(d["compare"]) <= 8 and d["compare"][0].get("is_self") is True, "compare: 5–8 rows, first is_self true")
    for c in d["compare"]:
        for k in ("fresh", "sweet", "strength"):
            need(isinstance(c.get(k), int) and 1 <= c[k] <= 5, f"compare {c.get('name')}: {k} 1–5")
    need(5 <= len(d["authenticity"]) <= 8, "authenticity: 5–8 rows")
    need(5 <= len(d["faq"]) <= 8, "faq: 5–8 rows")
    need(3 <= len(d["sources"]) <= 10, "sources: 3–10")
    for s in d["sources"]:
        need(str(s.get("url", "")).startswith("https://") and s.get("label"), f"source needs label and https url: {s}")
    text = json.dumps({k: v for k, v in d.items() if k not in ("query",)}, ensure_ascii=False)
    for word, fix in BANNED.items():
        need(word not in text, f"found '{word.strip()}' — {fix}")
    return out


if __name__ == "__main__":
    doc = json.load(open(sys.argv[1], encoding="utf-8"))
    found = problems(doc)
    if found:
        print("\n".join("✗ " + p for p in found))
        sys.exit(1)
    print(f"✓ {doc['name']} — ready to save ({len(json.dumps(doc, ensure_ascii=False)):,} characters)")
