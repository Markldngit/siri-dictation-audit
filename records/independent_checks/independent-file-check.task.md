You are an independent auditor. You know nothing about how these files were made. Your job: find what is missing, wrong, or unsupported. Do not fix anything; report only.

Files: /home/claude/siri-audit/ (sources.json, switches.json, touchpoints.json, pairings.json, findings.json, schema.json, check.py). pairings.json is large; use Python to query it rather than reading it whole. Start by running `python3 /home/claude/siri-audit/check.py` and reading the other files.

Purpose of the files: for an iPhone 14 Plus on iOS 26.7 (no Apple Intelligence), record every user switch that affects Siri, Dictation, Siri Suggestions or Search; every kind of data ("touchpoint") those features touch; and, for every switch x touchpoint x feature, whether Apple's own privacy pages say turning the switch off stops it, say it continues, or are silent. Evidence ids (E01...) point to a short verbatim locator phrase on an Apple page plus a paraphrase.

Read Apple's pages word-for-word yourself. Use the built-in browser tools: load them with ToolSearch query "mcp__remote-devices__Claude_Browser__" (max_results 64). apple.com is already approved. Open https://www.apple.com/legal/privacy/data/en/ask-siri-dictation/ with preview_start, then use javascript_tool to fetch other pages from the same origin (fetch, DOMParser, querySelector("main"), textContent). Do not use WebFetch; it summarises. If the browser tools can't be reached, say so and do only the file-internal checks.

Minimum pages to read in full: ask-siri-dictation, improve-siri-dictation, siri-suggestions-search, location-services, health-app (all under /legal/privacy/data/en/). Read others listed in sources.json as needed.

Check and report, with specifics (ids, quotes of at most ~12 words from Apple):
1. Switches or controls Apple names on those pages that are missing from switches.json.
2. Kinds of data Apple says Siri/Dictation/Suggestions/Search use that are missing from touchpoints.json.
3. Cells in pairings.json with apple.status "stops" or "continues" where the cited evidence does not actually support that status (check every non-"not_stated" cell; there are about 109).
4. Places where "not_stated" is wrong because Apple does say something.
5. Paraphrases in sources.json evidence that misstate the Apple sentence.
6. Anything in flows_without_switch that is wrong or missing.
7. Anything in findings.json inconsistent with the grid.
8. Weaknesses in check.py (things it would fail to catch).
Rank findings by severity: errors (wrong claims) first, then omissions, then minor. Be concise.