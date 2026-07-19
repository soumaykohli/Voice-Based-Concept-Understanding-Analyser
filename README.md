# Voice-Based Concept Understanding Analyser (VBCUA)

## Overview

The Voice-Based Concept Understanding Analyser (VBCUA) is a significant advancement in AI-assisted educational assessment, offering a scalable, objective, and transparent method for evaluating spoken conceptual explanations. By integrating technologies such as OpenAI Whisper for transcription and Sentence-BERT for semantic similarity, the system moves beyond traditional, subjective manual evaluations. It provides a holistic assessment by analyzing not only the content accuracy but also delivery quality through metrics like filler word usage, pause ratios, and signal energy.

Built on a modular architecture using Streamlit, VBCUA provides an accessible, real-time environment for students, educators, and researchers. The platform's ability to generate structured PDF reports—complete with waveforms, evaluation tables, and qualitative feedback (Strong, Moderate, or Poor understanding)—ensures that users receive actionable insights to strengthen their conceptual mastery and communication skills. This combination of deterministic metrics and AI-driven analysis promotes consistency and fairness across all evaluations.

VBCUA is designed as an educational tool to support rather than replace human judgment. Future potential for the platform includes:

Multi-concept evaluation to assess broader subject matter.

Progress tracking to monitor individual learner growth over time.

Multilingual support to increase accessibility for diverse learners.

Real-time voice input for immediate feedback during live practice.

Adaptive feedback to provide personalized guidance based on specific performance.

Ultimately, the VBCUA project demonstrates how responsibly designed AI can empower learners with meaningful feedback while maintaining educational integrity and transparency

## Features

- Speech-to-text transcription
- Semantic similarity evaluation
- Audio feature extraction
- Filler word detection
- Waveform visualization
- Understanding score generation
- PDF report generation

---

## Technologies

- Python
- Streamlit
- Whisper
- Sentence-BERT
- Librosa
- ReportLab

---


**Deployed URL(Streamlit Community Cloud):**

👉 **[Access the Deployment] https://voice-based-concept-understanding-analyser-gh3u9lyi9cnzn8vlpv5.streamlit.app/**

## Installation

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

## Project Structure

```
VBCUA/
├── app.py
├── model_loader.py
├── speech_to_text.py
├── semantic_eval.py
├── audio_utils.py
├── text_utils.py
├── scoring_engine.py
├── report_generator.py
├── uploads/
├── reports/
├── temp/
└── tests/

```
