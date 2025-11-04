word1 = input().strip().lower()
word2 = input().strip().lower()

if sorted(word1) == sorted(word2):
    print("ДА")
else:
    print("НЕТ")
