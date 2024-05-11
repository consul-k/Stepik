hell_set = frozenset(int('6' * i) for i in range(1, 667))
print(' '.join(str(x) for x in sorted(hell_set)))
