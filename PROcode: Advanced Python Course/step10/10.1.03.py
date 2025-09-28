a = set(input().split())
b = set(input().split())

res1 = ', '.join(sorted(a & b))
res2 = ', '.join(sorted(a - b))

print('Общие: {' + res1 + '}')
print('Чистые охотники: {' + res2 + '}')
