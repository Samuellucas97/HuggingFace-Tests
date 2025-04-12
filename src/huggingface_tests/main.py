from transformers import pipeline

summarize_model = pipeline("summarization", model="facebook/bart-large-cnn")

MAX_LENGTH=100
MIN_LENGTH=20
DO_SAMPLE=False

uni_description = """As a national graduate education institution that specializes in teaching and research in advanced science and technology, NAIST tackles problems at the frontiers of science in an environment of interdisciplinary and international cooperation. Students and researchers have access to world-class facilities in a stimulating environment, integrating individual research achievements with collaboration between different fields and offering a globally flexible education for scientists and engineers. In the evaluations issued by the Japanese government in 2022, NAIST was one of only two top-ranked national universities in Japan in respect to both research and education."""

response = summarize_model(uni_description, min_length=MIN_LENGTH, max_length=MAX_LENGTH, do_sample=DO_SAMPLE)

print(response) 