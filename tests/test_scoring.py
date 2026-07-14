from scoring_engine import *

audio = {

    "pause_ratio":0.12,

    "rms_energy":0.031

}

print(

    evaluate_understanding(

        92,

        0.02,

        audio

    )

)