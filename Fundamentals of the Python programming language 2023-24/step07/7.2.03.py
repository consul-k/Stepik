word = input().split()
dict = {i:word.count(i) for i in word}
for key in sorted(dict):
    print(key, dict[key])
