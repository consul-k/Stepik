import ast
import sys

input_data = sys.stdin.read().strip()
scores = ast.literal_eval(input_data)

min_score = min(scores.values())

filtered_scores = {id: score for id, score in scores.items() if score != min_score}

print(filtered_scores)
