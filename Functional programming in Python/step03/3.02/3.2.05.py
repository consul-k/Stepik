def find_longest_word_len(lst):
    max_len_word = [len(i) for i in lst]
    return max(max_len_word)
