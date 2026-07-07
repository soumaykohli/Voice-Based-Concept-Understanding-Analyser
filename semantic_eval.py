import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ----------------------------------------------------
# Load Sentence-BERT Model (Cached)
# ----------------------------------------------------

@st.cache_resource
def load_sbert_model():
    """
    Loads the Sentence-BERT model once during the Streamlit session.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


from model_loader import load_sentence_bert

model = load_sentence_bert()


# ----------------------------------------------------
# Generate Embeddings
# ----------------------------------------------------

def generate_embeddings(student_text, reference_text):
    """
    Generates sentence embeddings for both the student's
    explanation and the reference concept.
    """

    student_embedding = model.encode(
        student_text,
        convert_to_numpy=True
    )

    reference_embedding = model.encode(
        reference_text,
        convert_to_numpy=True
    )

    return student_embedding, reference_embedding


# ----------------------------------------------------
# Semantic Similarity
# ----------------------------------------------------

def semantic_similarity(student_text, reference_text):
    """
    Computes cosine similarity between the student's
    explanation and the reference concept.

    Returns:
        float : similarity percentage (0–100)
    """

    student_embedding, reference_embedding = generate_embeddings(
        student_text,
        reference_text
    )

    similarity = cosine_similarity(
        [student_embedding],
        [reference_embedding]
    )[0][0]

    # Convert cosine similarity to percentage
    score = max(0, similarity) * 100

    return round(score, 2)


# ----------------------------------------------------
# Similarity Interpretation
# ----------------------------------------------------

def similarity_level(score):
    """
    Returns a qualitative interpretation of the
    semantic similarity score.
    """

    if score >= 85:
        return "High Conceptual Similarity"

    elif score >= 60:
        return "Moderate Conceptual Similarity"

    return "Low Conceptual Similarity"


# ----------------------------------------------------
# Complete Evaluation
# ----------------------------------------------------

def evaluate_semantics(student_text, reference_text):
    """
    Returns both the semantic similarity score and
    its qualitative interpretation.
    """

    score = semantic_similarity(
        student_text,
        reference_text
    )

    level = similarity_level(score)

    return score, level


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    reference = (
        "Machine Learning is a subset of Artificial Intelligence "
        "that enables systems to learn from data without being "
        "explicitly programmed."
    )

    student = (
        "Machine learning allows computers to learn from data "
        "without direct programming."
    )

    score, level = evaluate_semantics(
        student,
        reference
    )

    print(f"Semantic Score : {score}%")
    print(f"Evaluation     : {level}")