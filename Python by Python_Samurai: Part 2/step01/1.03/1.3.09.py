l = input()
a = input().split()
for word in a:
    if l in word.lower():
        print(word, end = ' ')
