text = input()
result = ''.join([char for index, char in enumerate(text) if index % 3 != 0])
print(result)
