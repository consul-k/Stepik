word = input().split()
w1 = set(word[0])
w2 = set(word[1])
w3 = set(word[2])
if w1 == w2 == w3:
    print('YES')
else:
    print('NO')
