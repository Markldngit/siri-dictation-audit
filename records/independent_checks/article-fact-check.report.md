I found 12 problems in the draft that need fixing before it's published. Everything else checks out: all 13 Apple and phone quotes match their sources exactly (str.count = 1, right page and date), and 33, 9, 24, 70, 13, 226, 985, 935, "four tests" and the 14 Sep / 30 Oct page dates all recompute correctly. Both checking programs report no problems.

**Unsupported claims**

1. **"In September I turned Siri off exactly as Apple said."** and the 26 Sep table cell **"Both switched off: Siri off by Apple's definition (my screenshots on 1 Nov confirm both)."**
   - In findings F1 and F2 (26 Sep), Talk to Siri and the side-button switch are "not recorded". The only Sept record is your statement that Learn from this App was off for Contacts. Both Siri switches are first shown off on 1 Nov (O007, F3).
   - Fix: "By 1 November both were off (my screenshots)." Drop the September claim, or move the "Both switched off" cell to a 1 Nov row.

2. **"I added Contacts."** (step 3) and **"put Contacts on Apple's new list"** (intro)
   - O106 records only that Contacts is on the Excluded Apps list. Its note says nothing seen shows whether you added it or the update carried it over from your iOS 26 setting.
   - F4's notes say "added", which contradicts O106.
   - Fix: "Contacts was on the Excluded Apps list (I confirmed it)", unless you confirm you added it yourself and that is recorded.

3. **"It happened again on 1 November."** (the word said was "Kimi")
   - F3 says you "did not restate" the words you spoke. O009 is still marked "pending" for that statement.
   - Fix: record your statement in F3/O009 first, or soften to "a similar test on 1 November".

4. **"There is no "Turn Off Siri" anywhere on my phone."**
   - The screenshots cover only the Settings > Siri screens (O002–O004, `not_seen_on_this_phone`).
   - Fix: "There is no "Turn Off Siri" in Settings > Siri on my phone."

5. **"It names no switch that stops this, short of turning Siri and Dictation off entirely."**
   - The Sept page never says that turning Siri and Dictation off stops this data being sent. It only says on-device transcripts are deleted.
   - The same sentence links the data to "third-party apps you allow to integrate with Use with Siri Requests", and the page also lists a Screen Time restriction.
   - Fix: "It ties no switch to this data, and doesn't say that turning Siri and Dictation off stops it."

6. **"I read Apple's UK pages. The US edition may be worded differently."**
   - Only the User Guide pages are the UK edition (en-gb; `records/edition_check.json`).
   - The privacy pages are Apple's single English edition, /legal/privacy/data/en/ (marked `lang="en-US"`), with no UK/US split (`checkpoint.json` line 329). The values pages are apple.com/privacy/ (en-US).
   - Fix: "I read Apple's UK edition of the iPhone User Guide; the US edition of the guide may be worded differently. The privacy pages exist in one English edition."

7. **"That covers 117 Apple privacy pages"**
   - 117 is the number of pages screened (`sources.json`). The snapshots/ folder holds 118 apple.com/legal/privacy/data pages, and `checkpoint.json` says 118. There are also 5 values pages, captured 3 Nov.
   - Fix: "118 Apple privacy pages (plus 5 of Apple's privacy-values pages)", or reconcile the count in the records.

**Misquote and overstatement**

8. **'…your device may send other contextual data to Apple", including "Contact names, nicknames, and relationships"'**
   - Apple actually writes "…to Apple, including from third-party apps you allow to integrate with Use with Siri Requests, such as: Contact names, nicknames, and relationships (for example, “my dad”), if you set them up in your contacts".
   - Fix: replace "including" with "such as", or quote the full clause.

9. **"a company name, which isn't on Apple's list."**
   - Both Apple lists are introduced with "such as", so they are examples, not complete lists.
   - Fix: "a company name, which isn't among the examples Apple gives." The same applies to "It was a company name" in step 2.

10. **"The off switch for Siri moved between versions without notice."** and **"By November, Apple said something different, and nothing told me."**
    - No record supports "without notice". It is your experience, not something the records show.
    - Fix: "and I saw no notice of the change." Also note that the rewritten page is dated 30 Oct but was captured on 1 Nov.

11. **Values table**
    - Putting "When Apple does collect personal data, we’re clear and transparent about it." next to "Apple rewrote its Siri privacy page on 30 October, for a version of iOS I wasn't running." implies bad faith.
    - The rewritten page doesn't mention an iOS version.
    - Fix: "Apple's page dated 30 October describes controls (Turn Off Siri, Excluded Apps) that my phone, on iOS 26.7.1, didn't have."
    - Smaller points, change if you want to be strict:
      - **"an ordinary reader would expect"**: the 226 figure is Claude's judgement (`layer_meaning.reasonable_reader`), so present it as "by my assessment".
      - **"For 9 of them, Apple says what turning them off does to my data"**: for one of the 9 (the side-button switch) the stated effect applies only as a step in turning Siri and Dictation off.

**Personal data (for the published audit, not the draft text)**

12. The draft itself names no employer or contact. But the promised "full audit… published at [link]" and the "Screenshots from my phone" would reveal them:
    - The employer's name appears in `findings.json` F2–F4, in O009 and O112 (the dictation screenshots), in the [private screenshot] file name `[private screenshot]`, and in the [private screenshot] notes.
    - F1's output "[a contact's display name]" is an entry from a third party's contact card.
    - [private screenshot] shows third parties' names and must never be published, even redacted.
    - Your full name is on O002–O004 and O102; serial and model numbers are on O005 and O104.
    - The Excluded Apps list (O106–O107) shows the apps installed on your phone.
    - Fix: publish redacted copies (replace the employer with a placeholder, leave out [private screenshot], and black out the name and serial number) and say in the article that they are redacted.