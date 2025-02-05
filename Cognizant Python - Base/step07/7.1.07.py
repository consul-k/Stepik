words = input().split()
result = [(i, len(i)) for i in words]
print(result, dict(result), sep='\n')
