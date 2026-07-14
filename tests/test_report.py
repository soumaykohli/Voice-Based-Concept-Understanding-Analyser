from report_generator import *

generate_pdf(

    reference="Artificial Intelligence",

    transcript="Artificial Intelligence enables machines to learn.",

    similarity=91,

    filler_ratio=0.02,

    pause_ratio=0.15,

    rms_energy=0.031,

    score=95,

    level="Strong Understanding",

    waveform_path="temp/waveform.png",

    output_path="reports/test.pdf"

)