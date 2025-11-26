text1 = input().split()
text2 = input().split()

set1 = set(text1)
set2 = set(text2)

common_words = set1 & set2

print(sorted(list(common_words)))
