text = input()
result = dict(zip([i for i in text], [text.count(i) for i in text]))
print(result)
