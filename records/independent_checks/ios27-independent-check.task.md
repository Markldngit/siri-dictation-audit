You are an independent checker. You have not seen how this was made. Do NOT edit any file. No network. Work in /home/claude/siri-audit.

The folder ios27/ records what Apple's CURRENT text (privacy pages dated 2026-10-30; iOS 27 iPhone User Guide) says iPhone settings for Siri, Dictation, Search and Suggestions stop or leave on, for an iPhone 14 Plus on iOS 27.2. Rules it must meet (see ios27/brief_common.md):
- An Apple claim (apple_states stops/continues, or existing_data) in ios27/pairings_27.json may exist only where the cited sentence (ios27/sources_27.json evidence[X…].exact.text) explicitly states that effect for that setting, data (touchpoint), feature and action. stated_as must be right: direct_statement / purpose_of_instruction (a how-to stating its own purpose) / default_behaviour_page (names no switch; applies via the page's default-behaviour framing). A how-to naming no effect is not a claim. "Not stored" ≠ "not sent". "May review" ≠ reviewed by people.
- reasonable_reader entries are Claude's judgement and must be plausible readings of the cited Apple sentences.
- Claude's words (claude_note, note, reason) must not put quote marks around wording that is not Apple's exact wording.
- ios27/switches_27.json should list every relevant setting; settings Apple says need Siri AI / Apple Intelligence hardware are applies_to_this_phone false.

Do:
1. Run python3 -I ios27/check_27.py and python3 -I check.py; report last lines.
2. For EVERY Apple claim in ios27/pairings_27.json (about 40), read the cited sentences and say supported / partly / not supported, and whether stated_as is right. One line each.
3. Spot-check 25 random reader entries: is the reading plausible from the cited sentences?
4. Search ios27/source_index.json texts (Python) for settings relevant to Siri/Dictation/Search/Suggestions that switches_27.json missed. Report any.
5. Check findings.json F4 and records/observations/ios27_screens.json item X1 (cross_version_observations): is every statement supported by the screenshots' transcriptions and the cited Apple sentence? Flag anything overstated.
6. Look for quoted phrases in claude_note / note fields of ios27 files that are not Apple's exact words.

Report only problems, plus the step 2 list. Be concise.