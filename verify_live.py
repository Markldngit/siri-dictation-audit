#!/usr/bin/env python3
"""Check the quotes against Apple's live website.  Run:  python3 verify_live.py [ios26|ios27|values]
For each page, downloads it, reduces it to plain text and reports whether each quoted sentence is still there
word for word. Apple changes its pages, so 'not found' can mean Apple has reworded it since the capture date:
the capture date and fingerprint in the data files record what the page said then. A web archive copy of the
page from that date is the way to check older wording. Some sites block automated downloads; if so, open the
page in a browser and use Find."""
import hashlib, html, json, os, re, sys, time, urllib.request
H = os.path.dirname(os.path.abspath(__file__))
which = sys.argv[1] if len(sys.argv) > 1 else "ios27"
f = {"ios26": "data/ios26/apple_quotes.json", "ios27": "data/ios27/apple_quotes.json", "values": "data/apple_values.json"}[which]
d = json.load(open(os.path.join(H, f), encoding="utf-8"))
quotes = d.get("quotes") or {str(i): s for i, s in enumerate(d["statements"])}
norm = lambda s: re.sub(r"\s+", " ", s).strip()
def text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (audit verification)"})
    h = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    return norm(html.unescape(re.sub(r"<[^>]+>", " ", h)))
sq = lambda s: re.sub(r"\s+", "", s)   # spaces are ignored: turning tags into spaces leaves stray spaces before punctuation
sha = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
def present(q, t):
    """Short quote: the whole sentence must be in the page. Long quote (shown here as an excerpt): the excerpt must be in
    the page AND some stretch of the page containing it must match the full sentence's fingerprint, so a change
    anywhere in the sentence is caught."""
    if not q.get("quote_is_excerpt"): return sq(q["quote"]) in t
    loc, n, want = sq(q["locator"]), q["full_sentence_nospace_chars"], q["full_sentence_nospace_sha256"]
    i = t.find(loc)
    while i != -1:
        for a in range(max(0, i + len(loc) - n), i + 1):
            if sha(t[a:a + n]) == want: return True
        i = t.find(loc, i + 1)
    return False
cache, found, missing = {}, 0, []
for k, q in quotes.items():
    url = d["pages"][q["page"]]["url"]
    if url not in cache:
        try: cache[url] = sq(text(url)); time.sleep(1)
        except Exception as e: cache[url] = None; print("could not download", url, e)
    t = cache[url]
    if t is None: continue
    if present(q, t): found += 1
    else: missing.append((k, url))
print(f"{found} of {len(quotes)} quotes found word for word on Apple's live pages today.")
for k, u in missing: print("  not found today:", k, u)
