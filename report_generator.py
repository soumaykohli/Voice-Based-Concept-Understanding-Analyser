import os

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


# ----------------------------------------------------
# Feedback Generator
# ----------------------------------------------------

def generate_feedback(level):

    feedback = {

        "Strong Understanding":
        """
        The student demonstrates excellent conceptual understanding.
        The explanation is semantically aligned with the reference
        concept and exhibits strong communication skills with
        minimal filler words and appropriate speech confidence.
        """,

        "Moderate Understanding":
        """
        The student demonstrates a reasonable understanding of the
        concept. Some improvements are recommended in conceptual
        clarity, fluency, and reduction of filler words.
        """,

        "Poor Understanding":
        """
        The explanation indicates limited conceptual understanding.
        Additional study and practice are recommended to improve
        concept accuracy, fluency, and communication confidence.
        """

    }

    return feedback.get(
        level,
        "No feedback available."
    )


# ----------------------------------------------------
# PDF Generator
# ----------------------------------------------------

def generate_pdf(

    reference,

    transcript,

    similarity,

    filler_ratio,

    pause_ratio,

    rms_energy,

    score,

    level,

    waveform_path,

    output_path

):

    os.makedirs("reports", exist_ok=True)

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(output_path)

    elements = []

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "Voice-Based Concept Understanding Report",

            styles["Title"]

        )

    )

    elements.append(Spacer(1,20))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Reference Concept</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            reference,

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1,15))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Transcribed Explanation</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            transcript,

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1,15))

    # ------------------------------------------------

    if os.path.exists(waveform_path):

        elements.append(

            Paragraph(

                "<b>Waveform Visualization</b>",

                styles["Heading2"]

            )

        )

        elements.append(

            Image(

                waveform_path,

                width=450,

                height=150

            )

        )

        elements.append(Spacer(1,15))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Evaluation Metrics</b>",

            styles["Heading2"]

        )

    )

    table_data = [

        ["Metric","Value"],

        ["Semantic Similarity",f"{similarity:.2f}%"],

        ["Filler Word Ratio",f"{filler_ratio:.3f}"],

        ["Pause Ratio",f"{pause_ratio:.3f}"],

        ["Confidence (RMS Energy)",f"{rms_energy:.4f}"],

        ["Final Understanding Score",f"{score}/100"],

        ["Classification",level]

    ]

    table = Table(table_data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

            ("TEXTCOLOR",(0,0),(-1,0),colors.black),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ])

    )

    elements.append(table)

    elements.append(Spacer(1,20))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Qualitative Feedback</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            generate_feedback(level),

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1,15))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Summary</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "This report was automatically generated by the "
            "Voice-Based Concept Understanding Analyser (VBCUA). "
            "The evaluation combines speech transcription, "
            "semantic similarity, filler word detection, and "
            "audio feature analysis to assess conceptual "
            "understanding.",

            styles["BodyText"]

        )

    )

    # ------------------------------------------------

    document.build(elements)

    return output_path


# ----------------------------------------------------
# Standalone Testing
# ----------------------------------------------------

if __name__ == "__main__":

    generate_pdf(

        reference="Machine Learning is a subset of Artificial Intelligence.",

        transcript="Machine learning allows computers to learn from data.",

        similarity=91.35,

        filler_ratio=0.02,

        pause_ratio=0.12,

        rms_energy=0.031,

        score=95,

        level="Strong Understanding",

        waveform_path="temp/waveform.png",

        output_path="reports/sample_report.pdf"

    )

    print("PDF report generated successfully.")