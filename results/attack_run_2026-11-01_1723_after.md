# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-01 17:23
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `88d1cdcd-a51a-4043-af69-254982935590` | human | 0.470 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `7f239f98-efc1-4b79-8a69-efebd2d8fb0c` | unsure | 0.238 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9fce3e8c-e50c-4d3b-a98a-0abd40f164b3` | unsure | 0.041 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3c0b9155-7602-49d3-abd8-cbb01380dbf2` | unsure | 0.028 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0965d7df-ce21-4535-904b-86404dc86f86` | human | 0.432 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b5525061-a38a-4543-b926-0cd187f6c1e9` | human | 0.315 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b3968ad0-6607-45e3-be3b-04b878f7afb8` | unsure | 0.067 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `4dbecde6-41cb-49dd-9d91-02f5bbafaff1` | human | 0.421 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f78517ea-518b-4671-ada1-2d20d1b04fb5` | unsure | 0.016 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6ed6505d-28a5-461e-a65f-16ebef364d54` | ai | 0.438 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d73864b0-ae1e-465b-9315-27880f3c751a` | unsure | 0.062 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `89e56005-e5fb-48c3-9c0a-d95ffd0caebf` | unsure | 0.129 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `47980a7e-44a2-4e85-b594-15dc8619c3ab` | unsure | 0.158 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d269ccb7-e0ac-45d1-a6bc-de53fc934909` | unsure | 0.160 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `439db883-9fa6-4e52-9a96-f45cf706895d` | unsure | 0.229 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c8221a7d-649f-4ce8-a700-654ab18cc095` | unsure | 0.182 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `20397d2f-aaf9-45ff-ab03-aa556d59445a` | unsure | 0.221 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `2b320962-0104-43d3-bb74-d21e3b4cd664` | human | 0.337 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `9cfb33f2-ea72-4b6c-bc12-60ca3c80798d` | human | 0.347 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `af7f33ca-7873-467e-9652-e2dd3c8919b2` | human | 0.587 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4a99ca18-f33b-4bc4-a961-2ea390d834cb` | unsure | 0.111 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c4a5d1dd-ce2e-419a-8714-41e35ca0d121` | unsure | 0.203 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `914b1789-a002-491c-a02f-0569fb8f51fe` | unsure | 0.027 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `fd5c70e9-a059-414b-a848-1645c2a51549` | unsure | 0.119 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `fdd17dc7-7661-4641-a0f0-81c8b32a9774` | human | 0.667 |  |
| MF04 | malformed | text is only punctuation | 200 | `2c9b7ca5-2169-4b3c-bf30-f9b75f828718` | human | 0.322 |  |
| MF05 | malformed | text is a very long single word | 200 | `37d1ce02-47bb-4dea-8a35-a44ccd2d89a1` | ai | 0.331 |  |
| MF06 | malformed | text is emoji only | 200 | `b19722fe-9438-42c4-aad8-0d8d9a541e5a` | ai | 0.664 |  |
| MF07 | malformed | text is right-to-left script | 200 | `e35657bf-890f-44aa-b575-16db24327512` | ai | 0.573 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `361255f0-c9bd-443e-95c4-fb415b53daa1` | human | 0.397 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `b0caac36-e768-4fb8-be07-3e02c6ed1eb9` | human | 0.506 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9e2000f8-3b5b-4849-bd6b-7b7805097967` | human | 0.601 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `61514725-a854-4b60-b0cc-4c3e440d070d` | human | 0.601 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6ad0efac-89ef-490c-9561-bee3a699d0b9` | human | 0.601 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `85f1541d-549a-47b0-898b-38658fca4fa9` | human | 0.601 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1bfaebba-c354-473c-938e-061c0878b5cf` | human | 0.601 |  |
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
  "content_id": "88d1cdcd-a51a-4043-af69-254982935590",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.4704,
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
  "content_id": "7f239f98-efc1-4b79-8a69-efebd2d8fb0c",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.238,
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
  "content_id": "9fce3e8c-e50c-4d3b-a98a-0abd40f164b3",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0408,
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
  "content_id": "3c0b9155-7602-49d3-abd8-cbb01380dbf2",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0276,
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
  "content_id": "0965d7df-ce21-4535-904b-86404dc86f86",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.4318,
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
  "content_id": "b5525061-a38a-4543-b926-0cd187f6c1e9",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.315,
  "model_score": 0.5727,
  "style_score": 0.1123,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
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
  "content_id": "b3968ad0-6607-45e3-be3b-04b878f7afb8",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0674,
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
  "content_id": "4dbecde6-41cb-49dd-9d91-02f5bbafaff1",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.4214,
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
  "content_id": "f78517ea-518b-4671-ada1-2d20d1b04fb5",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0162,
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
  "content_id": "6ed6505d-28a5-461e-a65f-16ebef364d54",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.438,
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
  "content_id": "d73864b0-ae1e-465b-9315-27880f3c751a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0624,
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
  "content_id": "89e56005-e5fb-48c3-9c0a-d95ffd0caebf",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.1294,
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
  "content_id": "47980a7e-44a2-4e85-b594-15dc8619c3ab",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.1576,
  "model_score": 0.8051,
  "style_score": 0.3525,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
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
  "content_id": "d269ccb7-e0ac-45d1-a6bc-de53fc934909",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.1596,
  "model_score": 0.8329,
  "style_score": 0.3268,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
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
  "content_id": "439db883-9fa6-4e52-9a96-f45cf706895d",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.2294,
  "model_score": 0.8005,
  "style_score": 0.4288,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
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
  "content_id": "c8221a7d-649f-4ce8-a700-654ab18cc095",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.1818,
  "model_score": 0.8814,
  "style_score": 0.3004,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
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
  "content_id": "20397d2f-aaf9-45ff-ab03-aa556d59445a",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.221,
  "model_score": 0.8816,
  "style_score": 0.3394,
  "label": "We couldn't determine whether this text was written by a person or generated by AI. This result isn't a judgment about your work.",
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
  "content_id": "2b320962-0104-43d3-bb74-d21e3b4cd664",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3372,
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
  "content_id": "9cfb33f2-ea72-4b6c-bc12-60ca3c80798d",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3466,
  "model_score": 0.4625,
  "style_score": 0.191,
  "label": "We think this text is more consistent with human writing, but we can't be certain who wrote it.",
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
  "content_id": "af7f33ca-7873-467e-9652-e2dd3c8919b2",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5866,
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
  "content_id": "4a99ca18-f33b-4bc4-a961-2ea390d834cb",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.1108,
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
  "content_id": "c4a5d1dd-ce2e-419a-8714-41e35ca0d121",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.203,
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
  "content_id": "914b1789-a002-491c-a02f-0569fb8f51fe",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0266,
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
  "content_id": "fd5c70e9-a059-414b-a848-1645c2a51549",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1186,
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
  "content_id": "fdd17dc7-7661-4641-a0f0-81c8b32a9774",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.6668,
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
  "content_id": "2c9b7ca5-2169-4b3c-bf30-f9b75f828718",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3222,
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
  "content_id": "37d1ce02-47bb-4dea-8a35-a44ccd2d89a1",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.3308,
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
  "content_id": "b19722fe-9438-42c4-aad8-0d8d9a541e5a",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.6636,
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
  "content_id": "e35657bf-890f-44aa-b575-16db24327512",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.573,
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
  "content_id": "361255f0-c9bd-443e-95c4-fb415b53daa1",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.397,
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
  "content_id": "b0caac36-e768-4fb8-be07-3e02c6ed1eb9",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.5064,
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
  "content_id": "9e2000f8-3b5b-4849-bd6b-7b7805097967",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6008,
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
  "content_id": "61514725-a854-4b60-b0cc-4c3e440d070d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6008,
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
  "content_id": "6ad0efac-89ef-490c-9561-bee3a699d0b9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6008,
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
  "content_id": "85f1541d-549a-47b0-898b-38658fca4fa9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6008,
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
  "content_id": "1bfaebba-c354-473c-938e-061c0878b5cf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6008,
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
