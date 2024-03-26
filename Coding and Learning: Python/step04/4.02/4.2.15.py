from itertools import permutations

word = input()

perms = [''.join(p) for p in set(permutations(word))]
perms.sort()

for perm in perms:
    print(perm)
