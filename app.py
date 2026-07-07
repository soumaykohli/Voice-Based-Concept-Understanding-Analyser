import os
import streamlit as st

from speech_to_text import speech_to_text
from audio_utils import (
    extract_audio_features,
    save_waveform
)
from semantic_eval import semantic_similarity
from text_utils import filler_word_ratio
from scoring_engine import evaluate_understanding
from report_generator import generate_pdf


st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)


@st.cache_resource
def load_models():
    return True

load_models()


if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "similarity" not in st.session_state:
    st.session_state.similarity = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "level" not in st.session_state:
    st.session_state.level = ""

if "color" not in st.session_state:
    st.session_state.color = "#ffffff"

if "audio_features" not in st.session_state:
    st.session_state.audio_features = {}

if "waveform" not in st.session_state:
    st.session_state.waveform = ""

if "filler_ratio" not in st.session_state:
    st.session_state.filler_ratio = 0

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False


st.markdown("""
<style>

.main{
    padding-top:20px;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
}

.metric-box{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)


st.title("🎤 Voice-Based Concept Understanding Analyser")

st.caption(
    "Automated evaluation of spoken conceptual explanations using AI."
)

st.divider()


reference_answer = st.text_area(
    "Reference Concept",
    value="Machine Learning is a subset of artificial intelligence that allows systems to learn patterns from data and improve performance without being explicitly programmed.",
    height=120
)


left, right = st.columns([2,1])

with left:

    uploaded_audio = st.file_uploader(
        "Upload Student Audio",
        type=["wav","mp3"]
    )

with right:

    st.info(
        "Supported formats:\n\n"
        "- WAV\n"
        "- MP3"
    )


audio_path = None

if uploaded_audio is not None:

    os.makedirs("uploads", exist_ok=True)

    audio_path = os.path.join(
        "uploads",
        uploaded_audio.name
    )

    with open(audio_path,"wb") as f:

        f.write(uploaded_audio.read())

    st.audio(audio_path)


if uploaded_audio is not None:

    if st.button("Analyze Concept Understanding"):

        with st.spinner("Processing and evaluating..."):

            try:

                transcript = speech_to_text(audio_path)

                audio_features = extract_audio_features(audio_path)

                filler = filler_word_ratio(transcript)

                similarity = semantic_similarity(
                    transcript,
                    reference_answer
                )

                score, level, color = evaluate_understanding(
                    similarity,
                    filler,
                    audio_features
                )

                waveform = save_waveform(audio_path)

                st.session_state.transcript = transcript
                st.session_state.audio_features = audio_features
                st.session_state.similarity = similarity
                st.session_state.score = score
                st.session_state.level = level
                st.session_state.color = color
                st.session_state.waveform = waveform
                st.session_state.filler_ratio = filler
                st.session_state.analysis_complete = True

            except Exception as e:

                st.error(f"Processing failed.\n\n{e}")


if st.session_state.analysis_complete:

    st.success("Analysis Completed")

    st.divider()

    left,right = st.columns([2,1])

    with left:

        st.subheader("Transcribed Explanation")

        st.write(st.session_state.transcript)

    with right:

        st.subheader("Final Evaluation")

        st.metric(
            "Understanding Score",
            f"{st.session_state.score}/100"
        )

        st.markdown(
            f"""
            <h2 style="color:{st.session_state.color};">
            {st.session_state.level}
            </h2>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("Audio Visualization")

    st.image(
        st.session_state.waveform,
        use_container_width=True
    )

    st.divider()

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.metric(
            "Semantic Similarity",
            f"{st.session_state.similarity:.2f}"
        )

    with c2:

        st.metric(
            "Filler Word Ratio",
            f"{st.session_state.filler_ratio:.2f}"
        )

    with c3:

        st.metric(
            "Pause Ratio",
            f"{st.session_state.audio_features['pause_ratio']:.2f}"
        )

    with c4:

        st.metric(
            "Confidence (Energy)",
            f"{st.session_state.audio_features['rms_energy']:.4f}"
        )


    os.makedirs("reports",exist_ok=True)

    pdf_path = "reports/evaluation_report.pdf"

    generate_pdf(

        reference_answer,

        st.session_state.transcript,

        st.session_state.similarity,

        st.session_state.filler_ratio,

        st.session_state.audio_features["pause_ratio"],

        st.session_state.audio_features["rms_energy"],

        st.session_state.score,

        st.session_state.level,

        st.session_state.waveform,

        pdf_path

    )

    with open(pdf_path,"rb") as pdf:

        st.download_button(

            "📄 Download PDF Report",

            pdf,

            file_name="Evaluation_Report.pdf",

            mime="application/pdf"

        )

else:

    st.info("Upload an audio file to begin analysis.")