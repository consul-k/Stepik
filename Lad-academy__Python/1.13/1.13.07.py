def count_letters(phrase, letters):
    res = 0
    for c in phrase:
        if c in letters:
            res += 1
    return res

phrase = input()
letters = input().split()
print(count_letters(phrase, letters))
