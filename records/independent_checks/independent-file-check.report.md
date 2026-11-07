I read all 17 Apple pages that mention Siri or Dictation word-for-word in the built-in browser, including the five required ones, and scanned all 117 pages on the index. All 56 evidence locators appear verbatim on the page they name, and every page date in sources.json matches the page. `check.py` passes. Even so, several claims are wrong. `check.py --verify-live` could not check anything here because the sandbox proxy returns 403 for apple.com; that is an environment limit, not a data error.

## Errors: statuses the cited evidence does not support (item 3)

I checked all 109 non-"not_stated" cells.

1. **`analytics.improve_siri_dictation` × `search_queries` × `siri_requests` = stops (E32) is wrong.** E32 only says Siri searches are "still stored… if you have enabled Improve Siri & Dictation". Other Apple text says this storage is the default whether or not the switch is on:
   - E24: "Apple stores transcripts of your interactions with Siri".
   - E26: data kept for up to two years.
   - The search page: the Siri transcript "may be sent to Apple… and may be stored".
   
   It also contradicts the grid's own "continues" cell for `transcripts_apple_servers` under the same switch.
2. **"Stops sending" is mixed up with "stops storing".**
   - `improve_siri_dictation` × `audio` × `siri_requests`/`dictation` = stops. E22/E23 only say audio is not *stored*. E55/E23 say audio is still "sent to and processed on Apple servers", so the feature still touches it.
   - `search.help_improve_search` × `search_queries` × `search` = stops (E31). The same page says queries are still sent (E36/E37). It also says, with no condition on the switch, that Apple uses "your search queries to fine-tune Search models" and may send "a limited, randomly sampled set of search queries to search tools".
3. **`location.global` × `location_ip` × `siri_requests` = continues (E18, E42) is unsupported.** The cell's own note admits E42 is about "apps or websites" and that E18 mentions no switch. The same E18 evidence is treated as "not_stated" on `location.siri` × `location_ip`, which is inconsistent. `location.global` × `location_ip` × `search` has the same weakness, and E35 ("your location will not be sent to Apple") points the other way.
4. **`location.global` × `location_device` × `siri_requests`/`dictation` = stops rests on E35, a sentence from the Search page.** The Siri page says nothing about global Location Services. And if E35 is read broadly, it should also cover `siri_suggestions`, which is left "not_stated".
5. **Cells under `combo.siri_off`, `combo.siri_and_dictation_off` and `screen_time.siri_dictation` that no Apple text supports:**
   - `nearby_device_status` = stops. E29 describes sharing so that others can control *nearby devices "with Siri enabled"*. Nothing says turning Siri off on this iPhone stops it.
   - `voice_profile` = stops. The voice-setup audio sync (E15) is never tied to Siri being on or off.
   - More generally, E01, E02 and E20 are instructions for how to turn things off, not statements about what data stops. Every one of the roughly 90 "stops" cells built on them is an inference, not "Apple says". `combo.siri_off`'s own note admits that Type to Siri is not covered.
6. **`location.system.suggestions_search` × `location_device` × `siri_suggestions` = stops, but `location_device.used_by` has no `siri_suggestions` entry.** One of the two files is wrong. Apple does say "The location of your iPhone will be sent… more relevant recommendations", so `used_by` is the one to fix.

## Errors in paraphrases and flows (items 5 and 6)

- **E29 and flow N05** say no switch is named. Apple gates phone call status on "if you opted in to Personal Requests on HomePod".
- **N03** (request metadata, no switch): E30 itself gates the approximate-location part on "if you have turned on Location Services for Siri".
- **N06** (Search info, no switch): the location part has a switch (E34/E40).
- **E03** adds "only" ("deleted only when both… are off"). Apple does not say "only", and E04 is another way to delete.
- **E39** says "no Settings path given" but leaves out that Apple does describe the off state: "If you disable this option, the page will load normally."
- **E45** leaves out what the data actually is: Apple Account data "including text snippets from email messages".
- **Unsourced claim:** the `location.global` "continues" field includes emergency-call location, but no evidence id supports it.

## "not_stated" where Apple does say something (item 4)

- `location.siri` × `request_metadata` × `siri_requests` should be stops for the location part (E30).
- `improve_siri_dictation` × `transcripts_apple_servers` × `dictation` should be stops: Dictation "will not be stored unless you opt in" (E23). `used_by` omits `dictation`, so no status could be recorded.
- `improve_siri_dictation` × `contacts`/`installed_apps_shortcuts` should be stops for human review. E53 says a reviewer sees contact names and installed app names only for people who opted in.
- `siri.apps.learn_from_this_app` for Apple's own apps (Contacts, Mail, Messages, Safari) × the matching touchpoint × `siri_suggestions`: E08 applies to any app, but only `app_donated_data` is marked stops. This one is plausible, not certain.
- `safari.preload_top_hit`: Apple states the off behaviour, and the feature uses "bookmarks and browsing history". Neither is modelled.

## Missing switches and controls (item 1)

- **Personal Requests on HomePod** (ask-siri-dictation). Recognize My Voice on HomePod is also named there.
- **"Settings > Siri & Search"**, the only control named on the apple-store-app page ("To change how Siri accesses your information"). The source is listed but no switch comes from it.
- **Alerts & Shortcuts Automations** under System Services (location-services page): "an app or shortcut recommendation based on where you currently are".
- **Structural gap:** "Press Home for Siri" doesn't apply to this phone, which is fine. But Speech Recognition's effect ("the audio data to be transcribed may be sent to Apple") cannot be recorded, because no feature covers transcription for third-party apps. All of its cells are forced to "not_stated".
- **Unverified:** the 11 `guide.*` switches have no evidence and come from sources flagged `webfetch_not_verbatim_verified`. `guide.show_in_app` may duplicate `siri.show_in_*`.

## Missing kinds of data (item 2)

- **"Siri setup"** (ask-siri-dictation page header: "your audio, Siri setup, contacts, and location").
- **Siri settings and Siri Suggestions personalisation synced via iCloud (E14).** Without it, `icloud.siri` has nothing to stop in the grid.
- **Siri's responses** ("transcripts including your request and Siri's response").
- **Apple Account data and email snippets** used to improve Siri (iCloud Analytics).
- **Vocal Shortcuts and Voice Control audio** used to improve Siri (Improve Assistive Voice Features).
- **Health information spoken in a request Siri doesn't recognise as a Health request.** It is merged into `health` along with E44, but the switch doesn't stop it.
- **Text typed in Safari's search field, sent to the chosen search engine** (E38).
- **Bookmarks** (used by Preload Top Hit).
- **Visual search queries.** `search_queries` should say it includes them.
- **Minor:** `installed_apps_shortcuts` × `search` cites E37, which says "apps you use", not installed app names or shortcuts.

## Missing flows with no switch (item 6)

- Opening Safari sends Apple whether you use Safari search, plus device specs, on "longer-lived identifiers".
- Randomly sampled search queries go to search tools.
- Queries are used to fine-tune Search models, with no condition on any switch.
- "Suggestions may be used to personalize Apple services".
- Voice-setup audio sync (E15).
- The Improve Siri choice made at setup carries over to new devices.

## findings.json (item 7)

- F1 and F2 are recorded in the right cells, and their results match.
- `contacts_company` has an empty `used_by`, so the priority queue can never include it. E28 (personalised speech recognition "may leverage your on-device information") plausibly covers F1 and F2 with no switch, which weakens tying them to Learn from this App.
- F1 says which contact field produced the output is unknown, yet files it under `contacts` (names, nicknames, relationships).
- The findings record only one switch's state, not Siri, Dictation or on-device processing.
- The `switch_state` key `siri.apps.learn_from_this_app[Contacts]` is not a valid switch id, and nothing checks it.

## check.py weaknesses (item 8)

It does not check:
- that a cited evidence id is relevant, or comes from the switch's own source page;
- that "stops"/"continues" cells fall inside `used_by` (it would have caught error 6);
- that a finding's switch, touchpoint and feature match the cell citing it, that `observed.status` equals `finding.result`, or that `switch_state` keys are real switch ids;
- that in-scope switches have any evidence at all (the 11 `guide.*` switches have none);
- flows marked "no switch" against switches that exist;
- combos against their components;
- the `dimensions` block;
- duplicate ids: switches are keyed in a dict and `json.load` keeps only the last duplicate evidence key, so both go silently;
- that the `id` pattern in the schema is actually applied.

In addition:
- `--verify-live` covers only `browser_verbatim` sources, matches exact substrings (a locator spanning block tags could fail), never checks paraphrases, and depends on network access that isn't available here.
- Without `jsonschema` installed, it still reports "OK".