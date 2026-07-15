import os
import numpy as np
import librosa
import librosa.display

import matplotlib
matplotlib.use("Agg")  # Required for Streamlit Cloud

import matplotlib.pyplot as plt


# ----------------------------------------------------
# Audio Feature Extraction
# ----------------------------------------------------

def extract_audio_features(audio_path):
    """
    Extract useful audio-level features for evaluation.

    Features:
    - Duration
    - RMS Energy
    - Pause Ratio
    - Speech Rate (Estimated)
    """

    # Load audio
    y, sr = librosa.load(audio_path, sr=16000, mono=True)

    # -----------------------------
    # Duration
    # -----------------------------
    duration = librosa.get_duration(y=y, sr=sr)

    # -----------------------------
    # RMS Energy
    # -----------------------------
    rms = librosa.feature.rms(y=y)
    rms_energy = float(np.mean(rms))

    # -----------------------------
    # Pause Ratio
    # -----------------------------
    intervals = librosa.effects.split(y, top_db=25)

    speech_samples = sum(end - start for start, end in intervals)
    total_samples = len(y)

    if total_samples == 0:
        pause_ratio = 0.0
    else:
        pause_ratio = 1 - (speech_samples / total_samples)

    pause_ratio = round(max(0.0, pause_ratio), 3)

    # -----------------------------
    # Estimated Speech Rate
    # -----------------------------
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # Handle different librosa versions
    if isinstance(tempo, np.ndarray):
        tempo = float(tempo.item()) if tempo.size else 0.0
    else:
        tempo = float(tempo)

    return {
        "duration": round(duration, 2),
        "pause_ratio": pause_ratio,
        "rms_energy": round(rms_energy, 4),
        "speech_rate": round(tempo, 2)
    }


# ----------------------------------------------------
# Waveform Visualization
# ----------------------------------------------------

def save_waveform(audio_path):
    """
    Generate waveform image and save it.
    """

    os.makedirs("temp", exist_ok=True)

    y, sr = librosa.load(audio_path, sr=16000)

    plt.figure(figsize=(10, 3))

    librosa.display.waveshow(
        y,
        sr=sr,
        alpha=0.8
    )

    plt.title("Uploaded Audio Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.tight_layout()

    image_path = os.path.join(
        "temp",
        "waveform.png"
    )

    plt.savefig(
        image_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return image_path


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    sample_audio = "uploads/sample.wav"

    if os.path.exists(sample_audio):

        features = extract_audio_features(sample_audio)

        print(features)

        waveform = save_waveform(sample_audio)

        print(f"Waveform saved at: {waveform}")

    else:

        print("Sample audio not found.")
