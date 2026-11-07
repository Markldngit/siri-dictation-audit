#!/usr/bin/env python3
"""Check this audit folder. Run:  python3 check.py
Needs only Python 3. Checks that every file is internally consistent and recomputes the headline numbers.
It cannot check Apple's full pages (they are not published here, for copyright); verify_live.py checks the
quotes against Apple's live site instead."""
import hashlib, json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
def _nodup(pairs):
    ks = [k for k, _ in pairs]; d = {k for k in ks if ks.count(k) > 1}
    if d: problems.append(f"duplicate keys: {sorted(d)[:5]}")
    return dict(pairs)
L = lambda f: json.load(open(os.path.join(H, f), encoding="utf-8"), object_pairs_hook=_nodup)
sha = lambda b: hashlib.sha256(b).hexdigest()
problems = []
def bad(m): problems.append(m)

q26 = L("data/ios26/apple_quotes.json")["quotes"]; q27 = L("data/ios27/apple_quotes.json")["quotes"]
for name, q in (("iOS 26", q26), ("iOS 27", q27)):
    for k, v in q.items():
        if v["locator"] not in v["quote"]: bad(f"{name} quote {k}: locator not inside the quote")
        a, b = v["position_in_page_text"]
        if v.get("quote_is_excerpt"):
            if b - a != v["full_sentence_chars"]: bad(f"{name} quote {k}: position does not match the sentence length")
        else:
            if sha(v["quote"].encode()) != v["quote_sha256"]: bad(f"{name} quote {k}: text does not match its fingerprint")
            if b - a != len(v["quote"]): bad(f"{name} quote {k}: position does not match the quote's length")

def grid(path, quotes, used_key, label, phone=None):
    g = L(path); out = {"claims": 0, "switches_with_claims": set(), "gap": 0}
    used = {(u["touchpoint"], u["feature"]) for u in g.get(used_key, [])} if used_key else None
    for c in g["cells"]:
        if phone is not None and not phone.get(c["switch"], True): continue
        for a, s in c["by_action"].items():
            ap, rr = s["apple_states"], s["reasonable_reader"]
            claim = ap["status"] != "not_stated" or ap.get("existing_data")
            if claim:
                out["claims"] += 1; out["switches_with_claims"].add(c["switch"])
                for e in ap.get("evidence", []):
                    if e not in quotes: bad(f"{label}: {c['switch']} cites unknown quote {e}")
                if not ap.get("stated_as"): bad(f"{label}: {c['switch']} claim has no stated_as")
                if used is not None and (c["touchpoint"], c["feature"]) not in used: bad(f"{label}: {c['switch']} claim on data Apple does not say the feature uses")
            if rr["status"] == "expects_stops" and not claim: out["gap"] += 1
    return out

s27 = L("data/ios27/settings.json")["switches"]
phone = {s["id"]: s["applies_to_this_phone"] for s in s27}
r27 = grid("data/ios27/grid.json", q27, "used_by_27", "iOS 27 grid", phone)
r26 = grid("data/ios26/grid.json", q26, None, "iOS 26 grid")
ph = [s for s in s27 if s["scope"] == "in_scope" and s["applies_to_this_phone"]]
sw = [s for s in ph if s["kind"] == "switch"]

tests = {f["id"]: f for f in L("data/tests.json")["findings"]}
for gpath, key in (("data/ios26/grid.json", "switches_off"), ("data/ios27/grid.json", "ios27_switches_off")):
    seen = set()
    for c in L(gpath)["cells"]:
        for a, s in c["by_action"].items():
            for fid in s["observed"].get("findings", []):
                f = tests[fid]
                if c["switch"] not in f.get(key, []) or c["touchpoint"] != f["touchpoint"] or a != f["action"] or s["observed"]["status"] != f["result"]:
                    bad(f"{gpath}: observed cell does not match test {fid}")
                seen.add((fid, c["switch"]))
    for fid, f in tests.items():
        for s in f.get(key, []):
            if (fid, s) not in seen: bad(f"{gpath}: test {fid} not recorded for {s}")

for x in L("data/ios26/settings.json")["switches"]:
    for o in x.get("observed_routes", []):
        if sha(open(os.path.join(H, o["screenshot"]), "rb").read()) != o["published_sha256"]: bad(f"screenshot {o['id']} has changed")
for h in L("records/helpers_index.json")["helpers"]:
    for kind in ("task", "report"):
        p = os.path.join(H, "records", "independent_checks", f"{h['label']}.{kind}.md")
        if os.path.exists(p) and sha(open(p, encoding="utf-8").read().encode()) != h.get(kind + "_published_sha256"): bad(f"independent check {h['label']} {kind} has changed")
for obs in ("data/observations_ios26.json", "data/observations_ios27.json"):
    for i in L(obs)["items"]:
        if sha(open(os.path.join(H, i["file"]), "rb").read()) != i["published_sha256"]: bad(f"screenshot {i['id']} has changed")

s26 = [s for s in L("data/ios26/settings.json")["switches"] if s["scope"] == "in_scope"]
print("Headline numbers, recomputed from the data:")
print(f"  iOS 27.2 on this phone: {len(ph)} Siri-related items; Apple states a data effect for {sum(1 for s in ph if s['id'] in r27['switches_with_claims'])}")
print(f"  of which on/off switches: {len(sw)}; Apple states a data effect for {sum(1 for s in sw if s['id'] in r27['switches_with_claims'])}")
print(f"  places where a reader would expect a stop and Apple says nothing (iOS 27, this phone; Claude's assessment): {r27['gap']}")
print(f"  iOS 26 record (September): {len(s26)} items; Apple states a data effect for {len(r26['switches_with_claims'])}")
print(f"  Apple quotes: {len(q26)} (iOS 26) + {len(q27)} (iOS 27); tests: {len(tests)}")
# Every file must match the release manifest, and nothing may be added.
mp = os.path.join(H, "MANIFEST.json")
if not os.path.exists(mp): problems.append("MANIFEST.json is missing")
else:
    mraw = open(mp, "rb").read(); man = json.loads(mraw)["files"]
    IGNORE = (".git/", "__pycache__/")
    seen = set()
    for root, dirs, files in os.walk(H):
        for f in files:
            r = os.path.relpath(os.path.join(root, f), H).replace(os.sep, "/")
            if r == "MANIFEST.json" or f == ".DS_Store" or r.startswith(IGNORE) or "/__pycache__/" in r: continue
            seen.add(r)
            if r not in man: problems.append(f"{r}: not part of this release")
            elif hashlib.sha256(open(os.path.join(root, f), "rb").read()).hexdigest() != man[r]: problems.append(f"{r}: has changed since release")
    for r in man:
        if r not in seen: problems.append(f"{r}: missing")
    print(f"  release fingerprint (SHA-256 of MANIFEST.json): {hashlib.sha256(mraw).hexdigest()}")
    print("  compare it with the fingerprint published with the article")
print("OK: no problems found." if not problems else "PROBLEMS:\n  " + "\n  ".join(problems))
sys.exit(1 if problems else 0)
