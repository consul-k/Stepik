words = [input().strip() for _ in range(4)]

min_word = min(words)
max_word = max(words)

last_char_min = min_word[-1]
last_char_max = max_word[-1]

code_min = ord(last_char_min)
code_max = ord(last_char_max)

product = code_min * code_max
result = product ** 2

print(result)
