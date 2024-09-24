d1 = {}
d2 = {}

word1 = [word.strip('.,!?:;-') for word in input().lower().split()]
for word in word1:
    for l in word:
        if l in d1:
            d1[l] += 1
        else:
            d1[l] = 1

word2 = [word.strip('.,!?:;-') for word in input().lower().split()]
for word in word2:
    for l in word:
        if l in d2:
            d2[l] += 1
        else:
            d2[l] = 1
    
if d1 == d2:
    print('YES')
else:
    print('NO')
