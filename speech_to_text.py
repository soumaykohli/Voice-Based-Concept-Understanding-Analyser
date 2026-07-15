import os
import platform
import whisper
import librosa
import soundfile as sf
import streamlit as st

# ----------------------------------------------------
# Load Whisper Model (Cached)
# ----------------------------------------------------



@st.cache_resource
def load_whisper_model():
    """
    Loads the Whisper model only once during the Streamlit session.
    """
    return whisper.load_model("base")


from model_loader import load_whisper

model = load_whisper()


# ----------------------------------------------------
# Normalize Audio
# ----------------------------------------------------

def normalize_audio(audio_path):
    """
    Normalizes audio volume and resamples to 16 kHz
    for consistent Whisper transcription.
    """

    os.makedirs("temp", exist_ok=True)

    y, sr = librosa.load(audio_path, sr=16000)

    # Normalize amplitude
    y = librosa.util.normalize(y)

    normalized_path = os.path.join(
        "temp",
        "normalized_audio.wav"
    )

    sf.write(normalized_path, y, sr)

    return normalized_path


# ----------------------------------------------------
# Speech-to-Text
# ----------------------------------------------------

def speech_to_text(audio_path):
    """
    Converts speech audio into text using OpenAI Whisper.
    """

    try:

        normalized_audio = normalize_audio(audio_path)

        result = model.transcribe(
            normalized_audio,
            fp16=False
        )

        transcript = result["text"].strip()

        return transcript

    except Exception as e:

        raise RuntimeError(
            f"Speech transcription failed: {e}"
        )


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    sample_audio = "uploads/sample.wav"

    if os.path.exists(sample_audio):

        print("Transcribing...")

        text = speech_to_text(sample_audio)

        print(text)

    else:

        print("Place a sample audio file inside uploads/")
