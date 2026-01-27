s = input()
chars = list(s)
result = [chars[i] for i in range(len(chars)) if i % 2 == 0]
print(result)
