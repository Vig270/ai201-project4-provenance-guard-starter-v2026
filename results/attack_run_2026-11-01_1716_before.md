# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-01 17:16
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ceb5746a-458c-40a2-a19d-b952389daca9` | human | 0.551 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `681dd9c0-8eae-452f-9a8c-0fafb6a6f47c` | unsure | 0.067 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ef652b38-e45a-4a18-b1b2-1bef7eb87fb7` | unsure | 0.108 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b140d97a-e1be-4a0a-9558-951a8b177fc0` | unsure | 0.073 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `cb75628f-fd60-4e2a-bc24-4b28824df2ce` | human | 0.402 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `a8aadc22-b7c1-4fce-bf2f-31c9ca366a5d` | unsure | 0.131 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e5d9d59b-8b19-4702-b902-698ce2621883` | unsure | 0.109 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `cf9b84e9-8906-449c-adaf-d3ed1dd28da1` | human | 0.457 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `111a4077-d124-4ec1-8cfb-92c7fdf94676` | unsure | 0.154 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `b176014e-b155-42ae-978f-44d3c9fb7d81` | ai | 0.646 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b3f94a92-3ff8-4f4b-8bbc-2ed124f0e6a8` | unsure | 0.057 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `f86bfdb0-3126-4662-98d5-700d8a2db77f` | unsure | 0.269 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `2b10369f-d123-4a5b-9645-eda3a686e65a` | ai | 0.339 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `f0fff659-41a6-4ed2-bf92-a570407c1d82` | ai | 0.362 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `d5ffaac3-1347-4198-a3cb-edc9186a1fc3` | ai | 0.378 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `e53e8056-39a7-46cc-a362-8e12e99f39ba` | ai | 0.414 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `3e33d97a-dd50-4282-b80e-f37cdddf37af` | ai | 0.438 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `3010f278-0b99-4040-b7e7-81b3194734a2` | human | 0.344 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `86b9ba2d-e8a3-4edd-b35a-39150193d27f` | unsure | 0.238 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `359211c3-66d6-4c95-90c4-3e5289c2b81f` | human | 0.588 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `45eb5f83-5253-4106-a447-b74c5a28d930` | unsure | 0.009 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `ab3e4954-d0e6-4f7b-8e93-c04e06e0b50b` | unsure | 0.122 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8ba1abd6-3efa-4e4d-8398-8889302bd3b9` | unsure | 0.096 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e4a8af42-446b-44d4-8c75-a1c964ad4d99` | unsure | 0.025 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `e1c1c2b8-463b-45dc-8bfa-53b6e1b8bd03` | human | 0.800 |  |
| MF04 | malformed | text is only punctuation | 200 | `ecd9e131-c494-4d56-833c-602a3a8d5969` | human | 0.584 |  |
| MF05 | malformed | text is a very long single word | 200 | `1ad83bf6-42f5-47ff-bc46-34f34737763b` | ai | 0.597 |  |
| MF06 | malformed | text is emoji only | 200 | `9c621e37-45dc-4957-b3a6-a7d2dc7b6581` | ai | 0.796 |  |
| MF07 | malformed | text is right-to-left script | 200 | `39dbeefe-3f73-424b-a624-45323419d079` | ai | 0.669 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `bdec830a-b231-48b7-9707-1c8fa0dd5015` | human | 0.447 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `0cfac1e2-dda3-4c42-949f-264ed879b48f` | human | 0.664 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `738b8534-bf4a-4a64-b855-871353b19d27` | human | 0.738 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4fcce43e-e945-4ee0-8193-03f1988d3ebc` | human | 0.738 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e0d5a311-2c74-4401-8929-646398f8877f` | human | 0.738 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cb181cd7-46a5-4925-9ccf-3e0f963a9809` | human | 0.738 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `563887a1-9721-47e5-ba90-8d6a2f199180` | human | 0.738 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "ceb5746a-458c-40a2-a19d-b952389daca9",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.5514,
  "model_score": 0.1635,
  "style_score": 0.3661,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "681dd9c0-8eae-452f-9a8c-0fafb6a6f47c",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0674,
  "model_score": 0.5943,
  "style_score": 0.1676,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "ef652b38-e45a-4a18-b1b2-1bef7eb87fb7",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.1084,
  "model_score": 0.6662,
  "style_score": 0.293,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b140d97a-e1be-4a0a-9558-951a8b177fc0",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0726,
  "model_score": 0.6114,
  "style_score": 0.361,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "cb75628f-fd60-4e2a-bc24-4b28824df2ce",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.4022,
  "model_score": 0.3212,
  "style_score": 0.2469,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "a8aadc22-b7c1-4fce-bf2f-31c9ca366a5d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.1308,
  "model_score": 0.5727,
  "style_score": 0.1123,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "e5d9d59b-8b19-4702-b902-698ce2621883",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.1094,
  "model_score": 0.5862,
  "style_score": 0.4811,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "cf9b84e9-8906-449c-adaf-d3ed1dd28da1",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.4568,
  "model_score": 0.2452,
  "style_score": 0.3333,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "111a4077-d124-4ec1-8cfb-92c7fdf94676",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.1536,
  "model_score": 0.7042,
  "style_score": 0.2795,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "b176014e-b155-42ae-978f-44d3c9fb7d81",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6462,
  "model_score": 0.9792,
  "style_score": 0.4589,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "b3f94a92-3ff8-4f4b-8bbc-2ed124f0e6a8",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0566,
  "model_score": 0.6175,
  "style_score": 0.3201,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "f86bfdb0-3126-4662-98d5-700d8a2db77f",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.2686,
  "model_score": 0.7387,
  "style_score": 0.3907,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "2b10369f-d123-4a5b-9645-eda3a686e65a",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.3386,
  "model_score": 0.8051,
  "style_score": 0.3525,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "f0fff659-41a6-4ed2-bf92-a570407c1d82",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.3622,
  "model_score": 0.8329,
  "style_score": 0.3268,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "d5ffaac3-1347-4198-a3cb-edc9186a1fc3",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.378,
  "model_score": 0.8005,
  "style_score": 0.4288,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "e53e8056-39a7-46cc-a362-8e12e99f39ba",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.4142,
  "model_score": 0.8814,
  "style_score": 0.3004,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "3e33d97a-dd50-4282-b80e-f37cdddf37af",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.4378,
  "model_score": 0.8816,
  "style_score": 0.3394,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "3010f278-0b99-4040-b7e7-81b3194734a2",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3444,
  "model_score": 0.3223,
  "style_score": 0.3405,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "86b9ba2d-e8a3-4edd-b35a-39150193d27f",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.238,
  "model_score": 0.4625,
  "style_score": 0.191,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "359211c3-66d6-4c95-90c4-3e5289c2b81f",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5884,
  "model_score": 0.2044,
  "style_score": 0.2091,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "45eb5f83-5253-4106-a447-b74c5a28d930",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.009,
  "model_score": 0.5943,
  "style_score": 0.2949,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "ab3e4954-d0e6-4f7b-8e93-c04e06e0b50b",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.122,
  "model_score": 0.4998,
  "style_score": 0.2972,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "8ba1abd6-3efa-4e4d-8398-8889302bd3b9",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0962,
  "model_score": 0.6401,
  "style_score": 0.3333,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "e4a8af42-446b-44d4-8c75-a1c964ad4d99",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0246,
  "model_score": 0.5583,
  "style_score": 0.3231,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "e1c1c2b8-463b-45dc-8bfa-53b6e1b8bd03",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.8,
  "model_score": 0.0,
  "style_score": 0.3333,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "ecd9e131-c494-4d56-833c-602a3a8d5969",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.5844,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "1ad83bf6-42f5-47ff-bc46-34f34737763b",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.5966,
  "model_score": 0.9976,
  "style_score": 0.3333,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "9c621e37-45dc-4957-b3a6-a7d2dc7b6581",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7956,
  "model_score": 0.9969,
  "style_score": 0.6667,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "39dbeefe-3f73-424b-a624-45323419d079",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.669,
  "model_score": 0.9064,
  "style_score": 0.6667,
  "label": "We think this text may have been generated by AI, but this result isn't proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "bdec830a-b231-48b7-9707-1c8fa0dd5015",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.4466,
  "model_score": 0.2395,
  "style_score": 0.3636,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "0cfac1e2-dda3-4c42-949f-264ed879b48f",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.6644,
  "model_score": 0.0492,
  "style_score": 0.4444,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "738b8534-bf4a-4a64-b855-871353b19d27",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7376,
  "model_score": 0.0287,
  "style_score": 0.3704,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "4fcce43e-e945-4ee0-8193-03f1988d3ebc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7376,
  "model_score": 0.0287,
  "style_score": 0.3704,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "e0d5a311-2c74-4401-8929-646398f8877f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7376,
  "model_score": 0.0287,
  "style_score": 0.3704,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "cb181cd7-46a5-4925-9ccf-3e0f963a9809",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7376,
  "model_score": 0.0287,
  "style_score": 0.3704,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "563887a1-9721-47e5-ba90-8d6a2f199180",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7376,
  "model_score": 0.0287,
  "style_score": 0.3704,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
