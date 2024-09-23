d1 = {}
d2 = {}

word1 = input()
for i in word1:
    d1[i] = word1.count(i)

word2 = input()
for i in word2:
    d2[i] = word2.count(i)
    
if d1 == d2:
    print('YES')
else:
    print('NO')
