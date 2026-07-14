from semantic_eval import *

reference = "Machine Learning is a subset of Artificial Intelligence."

student = "Machine learning enables computers to learn from data."

print(

    evaluate_semantics(

        student,

        reference

    )

)