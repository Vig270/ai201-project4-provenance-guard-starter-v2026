# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. False positives - How often may a human's writing get called AI?

Of 10 pieces of writing I wrote myself, at most 1 should receive a high-confidence AI label in each trial.

**Why this target:**

I chose this target because falsely accusing a human writer of using AI could be unfair. I want the system to avoid incorrectly labeling genuine human writing as AI-generated.

---

## 2. Score spread - How far apart should clearly-AI and clearly-human text score?

The average score for 5 clearly AI-generated samples should be at least 0.2 higher than the average score for 5 clearly human-written samples in each trial.

**Why this target:**

I chose this target because AI-generated and human-written samples should show a measurable difference in their scores. A noticeable difference can help the system distinguish between the two, although the score alone cannot prove who wrote the text.

---

## 3. Label coverage - Is every one of your three labels actually reachable?

All 3 labels must appear at least once across the test samples in each trial.

**Why this target:**

I chose this target because the system should be able to represent different levels of certainty instead of assigning every submission the same label. This helps users understand that some results may be uncertain.

---

## 4. The appeal path - Does an appeal always change status and always get recorded?

All 5 valid appeal attempts must be recorded in the audit log, and each corresponding submission must change to `under_review`.

**Why this target:**

I chose this target because writers should have a fair chance to challenge a result they believe is incorrect. Recording every appeal makes the process traceable and accountable.

---

## 5. Bad input - What happens when `text` is missing, empty, or enormous?

Requests with missing or empty text, or text exceeding 10,000 characters, must receive a clear client-error response rather than a server-error response.

**Why this target:**

I chose this target because validating input can prevent unexpected errors and help the service handle invalid submissions safely instead of producing misleading results.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
