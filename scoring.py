"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

"""
Combine the model and style signals into one score, then assign a label.
"""


import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Weighted average:
    70% model signal + 30% style signal.

    Both inputs are expected to be between 0.0 and 1.0.
    """
    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    return round(max(0.0, min(1.0, combined)), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Return a machine-readable guess and a plain-language explanation.
    """
    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "This text has patterns associated with AI-generated writing, "
            "but this result is not proof of who wrote it.",
        )

    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "This text has patterns associated with human writing, "
            "but this result is not proof of who wrote it.",
        )

    return (
        "unsure",
        "The signals are inconclusive. This result cannot reliably determine "
        "whether a person or AI wrote the text.",
    )


def label_ranges() -> list[tuple[str, str]]:
    """Return the configured score ranges for each label."""
    return [
        ("high-confidence human", f"0.00 - {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} - {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} - 1.00"),
    ]