"""
Signal two: the style signal.

This signal measures writing patterns, not the meaning of the text.
Higher style scores indicate patterns that this simple heuristic treats
as more AI-like. It is not a reliable authorship detector.
"""

import re
import statistics
import sys


def sentences(text: str) -> list[str]:
    """Split text into sentences."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split text into lowercase words, with punctuation stripped."""
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    """Measure variation in sentence lengths, normalized to 0–1."""
    sentence_list = sentences(text)
    lengths = [len(words(sentence)) for sentence in sentence_list]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    spread = statistics.pstdev(lengths) / mean_length
    return min(spread, 1.0)


def type_token_ratio(text: str) -> float:
    """Measure the proportion of words that are unique."""
    word_list = words(text)

    if not word_list:
        return 0.0

    return len(set(word_list)) / len(word_list)


def punctuation_density(text: str) -> float:
    """Measure punctuation marks per word, normalized to 0–1."""
    word_list = words(text)

    if not word_list:
        return 0.0

    punctuation_count = len(re.findall(r"[.!?,;:]", text))
    density = punctuation_count / len(word_list)

    return min(density, 1.0)


def style_signal(text: str) -> float:
    """Combine three simple features into a heuristic AI-likeness score."""
    spread = sentence_length_spread(text)
    diversity = type_token_ratio(text)
    punctuation = punctuation_density(text)

    low_sentence_variation = 1.0 - spread
    low_word_diversity = 1.0 - diversity

    return round(
        (low_sentence_variation + low_word_diversity + punctuation) / 3,
        4,
    )


if __name__ == "__main__":
    text = " ".join(sys.argv[1:])

    if not text.strip():
        print('Usage: python stylometry.py "some writing here"')
        sys.exit(1)

    print(f"{len(sentences(text))} sentences, {len(words(text))} words")
    print()
    print(f"sentence_length_spread   {sentence_length_spread(text):.4f}")
    print(f"type_token_ratio         {type_token_ratio(text):.4f}")
    print(f"punctuation_density      {punctuation_density(text):.4f}")
    print(f"style_signal             {style_signal(text):.4f}   (heuristic only)")