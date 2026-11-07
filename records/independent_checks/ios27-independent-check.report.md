I found problems in three places. Several Apple-claim notes no longer match their status, two reader notes put quote marks around words Apple didn't use, and X1 and F4 claim more than the screenshots and Apple's text support. I edited nothing.

## 1. Checkers
- `python3 -I ios27/check_27.py` ends with: `iOS 27: 80 settings in scope; 14000 cells; 246 evidence sentences checked; 40 Apple statements` / `OK: no problems found.`
- `python3 -I check.py` (the iOS 26 record) ends with: `OK: no problems found.`

## 2. Apple claims (40)
"OK" means the stated_as label is right.

1. siri_or_hey_siri / audio / siri_requests / used_on_device, stops, direct. **Partly.** X175 says only that the phone stops listening for the activation phrase. Treating that as "audio used_on_device stops" is Claude's mapping; the note admits this. OK.
2–5. press_side_button and type_to_siri_requests (siri_requests and dictation), deleted, direct (X173/X174/X168). **Partly.** Apple states deletion only when Siri and Dictation are both disabled; this switch is just one step. The condition says so. OK.
6. excluded_apps / app_donated_data / siri_suggestions, stops, purpose (X176). **Supported.** The third clause ("using data from an app to make suggestions across other apps") carries it. X029, X176 and X177 are the same sentence cited three times. OK.
7. app_clips.learn / app_donated_data / siri_suggestions, stops, purpose (X191). **Partly.** Apple says "personalize Siri", not suggestions, and doesn't say app clips are installed apps. OK.
8–9. turn_off_siri, deleted, purpose (X192/X193). **Supported.** OK. But the note says "stops is used…" while the status is not_stated (see problem A).
10. use_siri_classic / search_queries / siri_requests / sent_to_apple, continues, direct (X206/X207). **Partly.** Apple says "may be sent". The sentence names no Use Siri Classic switch; it follows an "If you do not choose to enable Siri AI" sentence. That is closer to a conditional statement or default behaviour than a direct statement about this switch.
11–12. siri_ai_turn_off, deleted, purpose (X192/X193). **Partly.** It is linked to Siri AI only through the guide (G27:iph3fed3f2c3). OK. Same stale note as 8–9.
13–14. combo.siri_and_dictation_off, deleted, direct (X194/X168). **Supported.** OK. The note says "stops is the closest allowed status", but the status is not_stated.
15, 17, 22, 24. improve_siri_dictation and improve_siri_ai / audio / stored_by_apple, stops, direct (X195), on condition both are off. **Supported.** OK.
16, 18, 23, 25. Same two switches / audio / sent_to_apple, continues, default_behaviour_page (X196/X197/X198). **Supported** with the on-device condition. OK. (The O101 footer says on-device processing is indicated on this phone, so the condition isn't met there.)
19, 20, 26, 27. request_metadata / stored_by_apple, continues, default page (X180). **Supported.** OK.
21, 28. search_queries / siri_requests / stored, continues, default page (X181). **Supported.** OK.
29. help_improve_search / search_queries / siri_requests / stored, continues, direct (X201/X202). **Supported.** OK.
30. help_improve_search / search_queries / search / stored, stops, purpose (X199/X200). **Supported.** OK. It correctly says nothing about sending.
31–32. location_based_suggestions / location_device / sent, stops, direct (X203). **Supported** (precise location only). OK.
33. location.global / location_device / search / sent, stops, direct (X204). **Supported.** Small ambiguity: the sentence right before X204 is about the Suggestions & Search toggle. OK.
34–35. icloud.siri / siri_settings_sync / synced, stops, purpose (X205/X100). **Supported.** OK.
36–37. apps.show_in_app (Calendar) / email and messages / siri_suggestions / used_on_device, stops, purpose (X115). **Partly.** Apple states the purpose of turning it on; the off effect is inferred as the reverse. Treating that as purpose_of_instruction is a stretch.
38. apps.search_row (Mail) / email / search / used_on_device, stops, direct (X117). **Partly.** X117 is a description of the setting ("Allow content from Mail to appear in Search"); the off effect is again the inferred reverse.
39. news.show_in_app / safari_history / siri_suggestions, stops, direct (X213). **Supported.** OK.
40. health.access_health_data / health / siri_requests / used_on_device, stops, purpose (X125). **Supported.** Mapping "access" to used_on_device is a judgement call. OK.

**Problem A (stale notes):** `ios27/build_27.py` line 67 changes deletion-only claims from stops to not_stated, but copies the helper's note unchanged. So rows 8, 9, 11, 12, 13 and 14 in `ios27/pairings_27.json` say "stops is used" or "stops is the closest allowed status" when the status is not_stated.

## 3. Reader spot-check (25 random groups)
All 25 are plausible readings of the cited sentences. Two minor points:
- **enable_dictation:** one note expects stops across 26 cells (e.g. home_data, device_names, music_podcasts, item_labels) on the strength of X057 and X196 alone. Plausible, but broad.
- **Quoting:** see section 6.

## 4. Settings missing from switches_27.json
I found no relevant setting that is missing. "Location-Based Suggestions" is covered by `s27.search.location_based_suggestions`, and "Prioritize Moments with Contacts" by `s27.journaling_suggestions`. The other names that turned up aren't Siri, Dictation, Search or Suggestions settings: Weather's Suggested Locations, Predictive Text, Live Voicemail, Live Speech, and the Apple Intelligence Extensions sentence (a Siri AI item).

## 5. F4 and X1 overstate
**X1** (in `records/observations/ios27_screens.json`):
- Its main statement, "Apple's new main Siri control shows Siri as on after it", is given as fact. Apple's text presents Turn Off Siri as a row you tap and then confirm ("go to Settings > Siri > Turn Off Siri, then tap Turn Off Siri"; "Tap Turn Off Siri at the bottom, then tap Turn Off Siri"). No Apple sentence says the label shows whether Siri is on. "Main control" is Claude's own description.
- The quoted sentence ("If you have Siri AI but want to use the previous version of Siri, tap Turn On Siri…") is about Siri AI devices, which this phone isn't. It doesn't say the button reads Turn On Siri when Siri is off.
- The note "Apple labels the button 'Turn On Siri' when Siri is off" is an inference worded as an Apple fact.
- The nearest support on that same page is "Siri needs to be turned on before you can use it. If you didn't set up Siri… Tap Turn On Siri", and even that is only indirect.

**F4** (in `findings.json`):
- The note says "with Siri off", and `switches_off` includes `combo.siri_off` (the iOS 26 definition). But F4's own `ios27_not_set` says Turn Off Siri wasn't used, and X1 reads Siri as on. By Apple's iOS 27 wording, only the activation switches were off. That is overstated and contradicts itself.
- `ios27_not_set` rests on the button still being visible as evidence of state. That has the same weakness as X1; the sound basis is simply that the user didn't tap it.
- `ios27_switches_off` labels `s27.excluded_apps` and `s27.contacts.suggestions` as "off". What actually happened is Contacts was added to the exclusion list.
- Enable Dictation "on" is inferred; the note says so.
- Everything else in F4 is supported: the transcribed output (O112), Kimi being excluded (O107), the company field on other people's contact cards ([private screenshot]), and the four Suggestions switches being off (O108).

## 6. Quote marks around words that aren't Apple's
- 'found in Safari' (the reader note on `s27.apps.show_in_app` / safari_history, in both `ios27/pairings_27.json` and `ios27/proposals/reader27.json`). Apple wrote "found in Mail, Messages, and Safari".
- These three match Apple's words only if you ignore capitals: 'Stored on your device', 'Altogether' (Apple: "altogether") and 'The way you use Mail' (Apple: "the way you use Mail"), in the same two files.
- Quoted iOS 26 names and search strings in `switches_27.json` (e.g. 'Use with Siri Requests', 'Talk & Type', 'Reply Without Confirmation') are search terms or September names, so they're acceptable.