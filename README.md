# Siri, Dictation and my contacts: the audit

This folder is the evidence behind the article *"I turned it off. My iPhone kept listening to my contacts."* It lets anyone check the Apple quotes, the numbers and the tests in the article.

## What is here

| Folder or file | What it holds |
| --- | --- |
| `data/ios26/apple_quotes.json` | 148 sentences from Apple's privacy pages and the iOS 26 iPhone User Guide, as captured on 26 September 2026 |
| `data/ios27/apple_quotes.json` | 244 sentences from Apple's current privacy pages (5 of them rewritten and dated 30 October 2026, the rest unchanged since September and re-checked on 1 November) and the iOS 27 iPhone User Guide (captured 3 November 2026) |
| `data/changes_2026-09-26_to_2026-11-01.json` | For each September quote: still on Apple's page word for word on 1 November, or not |
| `data/apple_values.json` | Apple's own statements of its privacy values, captured 3 November 2026 |
| `data/ios26/settings.json`, `data/ios27/settings.json` | Every Siri-related setting, with Apple's name for it and Apple's route to it where Apple gives one |
| `data/ios26/grid.json`, `data/ios27/grid.json` | For each setting, kind of data, feature and action: what Apple says, what an ordinary reader would expect, and what my tests showed |
| `data/tests.json` | My four dictation tests, September to November 2026 |
| `data/observations_ios26.json`, `data/observations_ios27.json` | What each screenshot shows, transcribed |
| `screenshots/` | 17 screenshots from my phone, before and after the iOS 27 update (redacted) |
| `records/corrections.json` | Every change made to the data during the audit, with the reason |
| `records/independent_checks/` | Reports of the independent checks |
| `records/public_checker_tests.json` | Tests showing this folder's `check.py` catches deliberate changes |
| `records/tamper_tests.json`, `records/live_rechecks.json` | Tests of the audit's internal checkers, and re-checks of Apple's pages |
| `check.py` | Recomputes the headline numbers and checks the files are consistent |
| `verify_live.py` | Checks the quotes against Apple's live website |
| `MANIFEST.json` | The fingerprint of every file in this release |

Each quote gives a `page` key. The web address, capture time and fingerprints for that page are under `pages` at the top of the same file.

## How to check it

1. **Check a quote by hand.** Open the quote file in a text editor and search for a few words of the quote. Apple uses curly apostrophes and quote marks (’ “ ”), so search for words without punctuation. Note its `page` key, look it up under `pages` at the top for the web address, open that page and use Find. If the sentence is gone, Apple has reworded it since: a web archive copy from the capture date shows the earlier wording.
2. **Check the numbers.** Install Python 3, download this folder, open a terminal (Command Prompt on Windows) in the folder and run `python3 check.py` (on Windows: `py check.py`). It recomputes the article's numbers from the data, reports any inconsistency, and checks every file against `MANIFEST.json`, so any changed, added or missing file is reported. It prints the release fingerprint (the SHA-256 of `MANIFEST.json`): compare it with the fingerprint published with the article. If they match, you have exactly the files I published.
3. **Check all quotes against Apple's site.** Run `python3 verify_live.py ios27` (or `ios26`, or `values`). It needs an internet connection, and Apple may block automated downloads. It ignores spaces when comparing, because turning a web page into plain text can leave a stray space before punctuation that follows a link. For a long sentence shown here as an excerpt, it checks the whole sentence against its fingerprint, so a change anywhere in the sentence is caught. Expect `ios26` to report 34 quotes "not found": Apple rewrote those pages on 30 October 2026, which the article reports, and `data/changes_2026-09-26_to_2026-11-01.json` lists the same 34. Any other "not found" means Apple has changed the page since the capture date.

## Three layers, kept apart

- **What Apple says**: only Apple's exact words. An instruction like "go to Settings and turn off X" is not treated as a statement about data unless it states its own purpose ("To stop X, turn off Y"); then it is labelled that way.
- **What an ordinary reader would expect**: a judgement, made by an AI assistant (Claude), labelled in every entry.
- **What I saw**: my own tests and screenshots.

Fields named `paraphrase_claude`, `claude_note`, `note` and `reason` are Claude's words, not Apple's.

## Limits

- One iPhone 14 Plus, four tests. Your phone may behave differently.
- Apple's text doesn't say which route my contacts took into Dictation, and this audit can't either.
- On iOS 27 I hadn't used the new "Turn Off Siri" control when I ran the test.
- The iPhone User Guide pages are the UK edition; the US edition may be worded differently. The privacy pages exist in one English edition.

## What is not here, and why

- **Apple's full pages**, for copyright. Their fingerprints are recorded. The text fingerprint is of the page's main content reduced to plain text (scripts, styles, menus and footer removed; a space after each paragraph, list item, heading and table cell; runs of spaces collapsed), so it identifies the exact capture rather than being easy to reproduce by hand.
- **Long sentences in full.** A sentence over 300 characters is shown as an excerpt (`quote_is_excerpt`). Its `quote_sha256` and `full_sentence_chars` are those of the full sentence; `full_sentence_nospace_sha256` and `full_sentence_nospace_chars` are the same with all spaces removed, which `verify_live.py` uses.
- **Some screenshots.** One shows other people's contact cards. One is a duplicate. Three show only the list of apps on my phone.
- **Personal details.** A contact's display name, my former employer's name, my own name, a word from one test that may be a contact's nickname, and the names of other apps on my phone are replaced or blacked out. Each published screenshot carries the fingerprint of its unredacted original, which I keep privately. Where an independent-check report was redacted, its index entry says so and gives both fingerprints.

## Internal names

The data was built in a private folder, and some fields still name its files. They map to this folder like this:

| Name in the data | Here |
| --- | --- |
| `sources.json` | `data/ios26/apple_quotes.json` |
| `switches.json` | `data/ios26/settings.json` |
| `pairings_v2.json` | `data/ios26/grid.json` |
| `findings.json` | `data/tests.json` |
| `ios27/switches_27.json`, `ios27/sources_27.json`, `ios27/pairings_27.json` | `data/ios27/settings.json`, `data/ios27/apple_quotes.json`, `data/ios27/grid.json` |
| `records/observations/O…` | `screenshots/O….png` |
| Script and checker names (`scripts/…`, `ios27/check_27.py`, `check.py` in the records) | The private tools that built and checked the data; `check.py` here is the public checker |

## How it was made

The work was done with an AI assistant (Claude), directed by me. Apple's pages were captured through a browser on my own computer, word for word, with fingerprints. Every step that changed the data is in `records/corrections.json`, with the reason. Separate AI helpers that had not seen the work checked it independently, and their reports are in `records/independent_checks/`.
