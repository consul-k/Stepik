def ReverseComplement(dna):
    mapping = str.maketrans("ATGC", "TACG")
    res = dna.translate(mapping)
    return res[::-1]

dna = input()
print(ReverseComplement(dna))
