s = input().split()

p = [word for word in s if word == word[::-1]]

print(" ".join(p))
