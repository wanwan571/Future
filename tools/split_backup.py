"""Split a Studio backup into one JSON file per document, for ArtifactData `set` with `file_path`.

usage: python3 tools/split_backup.py data/perfume-studio-backup.json OUT_DIR
Writes OUT_DIR/perfumes/<id>.json and OUT_DIR/vs/<id>.json (without the "id" key) and prints them.
"""
import json
import os
import sys

src, out = sys.argv[1], sys.argv[2]
bk = json.load(open(src, encoding="utf-8"))
assert bk.get("format") == "perfume-review-studio-backup", "not a Studio backup"
for coll in ("perfumes", "vs"):
    os.makedirs(os.path.join(out, coll), exist_ok=True)
    for doc in bk.get(coll, []):
        doc = dict(doc)
        doc_id = doc.pop("id")
        doc.pop("photo", None)  # photos live in the old artifact's asset store and do not move
        path = os.path.join(out, coll, doc_id + ".json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"{coll}\t{doc_id}\t{path}")
