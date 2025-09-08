from fnmatch import fnmatch
for num in range(2234, 10**10 + 1, 2234):
    string = str(num)
    pattern1 = '4*5*6'
    pattern2 = '?74*68?'
    if fnmatch(string, pattern1) and fnmatch(string, pattern2):
        print(num, num // 2234)
