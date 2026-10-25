
## 1. Submission Path

1. A client sends a POST request to `/submit` with the text and creator ID in JSON format.
2. The service in `app.py` receives the request and extracts the submitted text and creator ID.
3. `detector.py` analyzes the text and calculates the model-based signal score.
4. `stylometry.py` measures patterns in the writing style and calculates the style score.
5. `scoring.py` combines both signal scores to produce an overall score.
6. The scoring component converts the overall score into a label, and `audit.py` records the decision and its supporting information.
7. The service returns a JSON response containing the content ID, guess, confidence, label, and both signal scores.


## 2. The Two Signals

### Signal 1: Detector (`detector.py`)

- **What it measures:** How predictable the submitted text is to a language model.
- **Why it might differ between human and AI writing:** AI-generated text may use common words and predictable sentence patterns.
- **Blind spot:** Human writers also use common words and simple sentences, so predictable writing does not prove that AI wrote it.

### Signal 2: Stylometry (`stylometry.py`)

- **What it measures:** Patterns and characteristics of the text's writing style.
- **Why it might differ between human and AI writing:** Human and AI writing may differ in sentence structure, punctuation, and other measurable style patterns.
- **Blind spot:** It cannot understand the meaning of the text. Changes such as typos, altered sentence structure, or inserted quotations can affect its measurements without changing who wrote the text.



## 3. False-Positive Scenario

A human student writes an original assignment using simple vocabulary and short sentences. Because the text is predictable, the detector gives it a score that makes the system suspect AI-generated writing. The system may assign a label that incorrectly flags the student's work.

The student may feel unfairly accused and lose trust in the system. The system should provide a clear explanation of the result, preserve the submission record, and allow the student to appeal the decision for review.

The scoring thresholds should be chosen carefully to reduce false accusations against genuine human writers. No single signal should be treated as proof of AI authorship.


## 4. Endpoint Contracts

### POST /submit

**Purpose:** Submit writing for analysis.

**Request fields:**
- `text`: The writing to analyze.
- `creator_id`: An identifier for the person submitting the writing.

**Expected response fields:**
- `content_id`: An identifier for the submitted content.
- `guess`: The system's overall assessment.
- `confidence`: The confidence score.
- `label`: The assigned category.
- `model_score`: The score from the model-based detector.
- `style_score`: The score from stylometry.

**Current status:** Not implemented. To be built in Milestones 3, 4, and 5.

### POST /appeal

**Purpose:** Allow a writer to challenge a previous result.

**Request fields:**
- `content_id`: The identifier of the submission being appealed.
- `reasoning`: The writer's explanation for the appeal.

**Expected behavior:**
- Check whether the content ID exists in the audit log.
- Record the appeal and move the item to `under_review`.
- Confirm the appeal to the writer.

**Current status:** Not implemented. To be built in Milestone 5.



