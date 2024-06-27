def count_letters(phrase, letters):
    cnt = 0
    for letter in phrase:
        if letter in letters:
            cnt += 1
    return cnt
