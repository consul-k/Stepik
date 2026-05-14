def CountNucleotides(dna):
    res = {'A': dna.count('A'), 'C': dna.count('C'), 'G':dna.count('G'), 'T':dna.count('T')}
    return res

dna = input()
print(*CountNucleotides(dna).values())
