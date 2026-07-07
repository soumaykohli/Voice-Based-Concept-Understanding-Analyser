# ----------------------------------------------------
# Scoring Engine
# ----------------------------------------------------

def evaluate_understanding(similarity, filler_ratio, audio_features):
    """
    Calculates the final understanding score based on:

    - Semantic Similarity (50%)
    - Filler Word Ratio (20%)
    - Pause Ratio (15%)
    - RMS Energy / Confidence (15%)

    Returns:
        score (int)
        level (str)
        color (str)
    """

    score = 0

    # ---------------------------------------
    # Semantic Similarity (50 Marks)
    # ---------------------------------------

    if similarity >= 90:
        score += 50

    elif similarity >= 80:
        score += 45

    elif similarity >= 70:
        score += 40

    elif similarity >= 60:
        score += 30

    elif similarity >= 50:
        score += 20

    else:
        score += 10

    # ---------------------------------------
    # Filler Word Ratio (20 Marks)
    # ---------------------------------------

    if filler_ratio <= 0.03:
        score += 20

    elif filler_ratio <= 0.06:
        score += 15

    elif filler_ratio <= 0.10:
        score += 10

    else:
        score += 5

    # ---------------------------------------
    # Pause Ratio (15 Marks)
    # ---------------------------------------

    pause_ratio = audio_features["pause_ratio"]

    if pause_ratio <= 0.15:
        score += 15

    elif pause_ratio <= 0.30:
        score += 10

    else:
        score += 5

    # ---------------------------------------
    # RMS Energy (15 Marks)
    # ---------------------------------------

    energy = audio_features["rms_energy"]

    if energy >= 0.03:
        score += 15

    elif energy >= 0.02:
        score += 12

    elif energy >= 0.01:
        score += 8

    else:
        score += 5

    score = min(score, 100)

    # ---------------------------------------
    # Classification
    # ---------------------------------------

    if score >= 80:

        level = "Strong Understanding"
        color = "#2ECC71"      # Green

    elif score >= 60:

        level = "Moderate Understanding"
        color = "#F39C12"      # Orange

    else:

        level = "Poor Understanding"
        color = "#E74C3C"      # Red

    return score, level, color


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    similarity = 91.8

    filler_ratio = 0.02

    audio = {

        "pause_ratio": 0.12,

        "rms_energy": 0.031

    }

    score, level, color = evaluate_understanding(

        similarity,

        filler_ratio,

        audio

    )

    print("Score :", score)

    print("Level :", level)

    print("Color :", color)