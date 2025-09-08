from fnmatch import fnmatch

for num in range(6718, 10 ** 9 + 1, 6718):
    if fnmatch(str(num), '?46?44*2'):
        print(num, num // 6718)
