def find_different_indexes(str1, str2):
    different_indexes = [i for i, (c1, c2) in enumerate(zip(str1, str2)) if c1 != c2]
    
    return different_indexes
