import streamlit as st
import whisper

from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# Whisper Model
# --------------------------------------------------

@st.cache_resource
def load_whisper():

    print("Loading Whisper Model...")

    return whisper.load_model("base")


# --------------------------------------------------
# Sentence-BERT Model
# --------------------------------------------------

@st.cache_resource
def load_sentence_bert():

    print("Loading Sentence-BERT...")

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )