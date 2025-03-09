def count_AGTC(dna_sequence):
    # Initialize counters for each nucleotide
    count_A = count_G = count_T = count_C = 0

    # Iterate over each character in the DNA sequence
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            count_A += 1
        elif nucleotide == 'G':
            count_G += 1
        elif nucleotide == 'T':
            count_T += 1
        elif nucleotide == 'C':
            count_C += 1

    # Return the counts as a tuple in the order A, G, T, C
    return (count_A, count_G, count_T, count_C)
