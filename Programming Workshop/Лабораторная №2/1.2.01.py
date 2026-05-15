def PatternToNumber(dna):
    s = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    res = 0
    for i in dna:
        res = res * 4 + s[i]
    return res

dna = input()
print(PatternToNumber(dna))
