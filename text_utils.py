import re

# ----------------------------------------------------
# List of Common Filler Words
# ----------------------------------------------------

FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "actually",
    "basically",
    "literally",
    "well",
    "so",
    "okay",
    "ok",
    "hmm",
    "you know",
    "i mean"
]


# ----------------------------------------------------
# Clean Text
# ----------------------------------------------------

def clean_text(text):
    """
    Converts text to lowercase and removes punctuation.
    """

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    return text


# ----------------------------------------------------
# Word Count
# ----------------------------------------------------

def word_count(text):
    """
    Returns the total number of words.
    """

    text = clean_text(text)

    words = text.split()

    return len(words)


# ----------------------------------------------------
# Count Filler Words
# ----------------------------------------------------

def count_filler_words(text):
    """
    Counts the number of filler words present in the transcript.
    """

    cleaned = clean_text(text)

    words = cleaned.split()

    filler_count = 0

    for word in words:

        if word in FILLER_WORDS:

            filler_count += 1

    return filler_count


# ----------------------------------------------------
# Calculate Filler Word Ratio
# ----------------------------------------------------

def filler_word_ratio(text):
    """
    Calculates the ratio of filler words to total words.
    """

    total_words = word_count(text)

    if total_words == 0:
        return 0.0

    fillers = count_filler_words(text)

    ratio = fillers / total_words

    return round(ratio, 3)


# ----------------------------------------------------
# Transcript Statistics
# ----------------------------------------------------

def transcript_statistics(text):
    """
    Returns useful transcript statistics.
    """

    total_words = word_count(text)

    fillers = count_filler_words(text)

    ratio = filler_word_ratio(text)

    return {

        "total_words": total_words,

        "filler_words": fillers,

        "filler_ratio": ratio

    }


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    sample = (
        "Um I think machine learning is actually a subset "
        "of artificial intelligence and it basically learns "
        "from data."
    )

    stats = transcript_statistics(sample)

    print(stats)