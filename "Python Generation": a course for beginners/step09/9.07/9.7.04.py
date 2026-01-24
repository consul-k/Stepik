max_weight = -1
heaviest_word = ""

for _ in range(4):
    word = input().strip()
    
    weight = sum(ord(char) for char in word)

    if weight > max_weight:
        max_weight = weight
        heaviest_word = word

print(heaviest_word)
