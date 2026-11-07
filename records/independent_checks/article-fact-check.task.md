You are an independent fact-checker. You have not seen how this was written. Do NOT edit any file. No network. Work in /home/claude/siri-audit.

Check the article draft at article/draft_2026-11-03.md against the audit records. It will be published; every factual statement must be supported.

Sources of truth:
- Apple quotes: snapshots/<page>.json (September), snapshots_2026-11-01/<page>.json (pages Apple changed; page dates in page_date_stamp), guide_pass_27/pages/*.json (iOS 27 guide), values/*.json (Apple privacy values pages). Field `text`.
- Phone observations: records/observations/ios26_screens.json, records/observations/ios27_screens.json (transcriptions of screenshots).
- Tests: findings.json (F1–F4).
- Counts: ios27/switches_27.json (scope in_scope, applies_to_this_phone, kind, apple_explicit_claims), ios27/pairings_27.json (layers), records/live_recheck.json, snapshots/ folder.

Do:
1. Every text in double quotes attributed to Apple or the phone: is it EXACTLY in the cited source (Python str.count)? Is it attributed to the right page/date?
2. Every number (33, 9, 24, 70, 13, 226, 117, 985, 935, four tests, dates, page dates): recompute from the files and confirm, or show the correct figure. For 226: count cells×actions where reasonable_reader expects_stops and apple_states not_stated with no existing_data, restricted to settings with applies_to_this_phone true.
3. Every factual claim (e.g. "It happened in September", "three people's cards", "There is no 'Turn Off Siri' anywhere on my phone" on iOS 26.7.1, "My two switches are still off", "Apple names no switch that stops this, short of turning Siri and Dictation off entirely", "a company name, which isn't on Apple's list"): supported, partly, or not supported — cite the record.
4. Anything that overstates, implies intent, or reveals personal data (names of third parties, serial numbers). The public version must not name the former employer or any contact.

Report only problems, each with the exact sentence and the fix. Be concise.