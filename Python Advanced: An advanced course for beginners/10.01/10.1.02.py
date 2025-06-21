a = set(input().split())

name1 = input()
name2 = input()
a.remove(name1)
a.add(name2)
print('{' + ', '.join(sorted(a)) + '}')
