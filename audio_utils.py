import os
import librosa
import librosa.display
import numpy as np
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

    # Load audio (convert to mono, 16 kHz)
    y, sr = librosa.load(audio_path, sr=16000, mono=True)

    # ---------------------------------------
    # Duration
    # ---------------------------------------

    duration = librosa.get_duration(y=y, sr=sr)

    # ---------------------------------------
    # RMS Energy
    # ---------------------------------------

    rms_energy = float(
        np.mean(
            librosa.feature.rms(y=y)
        )
    )

    # ---------------------------------------
    # Pause Ratio
    # ---------------------------------------

    intervals = librosa.effects.split(
        y,
        top_db=25
    )

    speech_length = sum(
        end - start
        for start, end in intervals
    )

    total_length = len(y)

    pause_ratio = 1 - (
        speech_length / total_length
    )

    pause_ratio = round(
        max(0, pause_ratio),
        3
    )

    # ---------------------------------------
    # Estimated Speech Rate
    # ---------------------------------------

    tempo, _ = librosa.beat.beat_track(
    y=y,
    sr=sr
)

if isinstance(tempo, np.ndarray):
    tempo = float(tempo[0]) if tempo.size > 0 else 0.0
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
    Generates a waveform image and saves it.
    """

    os.makedirs("temp", exist_ok=True)

    y, sr = librosa.load(audio_path)

    plt.figure(figsize=(10,3))

    librosa.display.waveshow(
        y,
        sr=sr
    )

    plt.title("Uploaded Audio Waveform")

    plt.xlabel("Time")

    plt.ylabel("Amplitude")

    plt.tight_layout()

    image_path = "temp/waveform.png"

    plt.savefig(
        image_path,
        dpi=300
    )

    plt.close()

    return image_path


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    sample_audio = "uploads/sample.wav"

    if os.path.exists(sample_audio):

        features = extract_audio_features(
            sample_audio
        )

        print(features)

        waveform = save_waveform(
            sample_audio
        )

        print("Waveform saved at:", waveform)

    else:

        print("Sample audio not found.")
