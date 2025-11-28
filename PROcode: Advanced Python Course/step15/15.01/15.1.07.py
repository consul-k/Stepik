def find_max_line(lines):
    max_words = 0
    result_line = ""
    
    for line in lines:
        words = line.split()
        word_count = len(words)
        
        if word_count > max_words:
            max_words = word_count
            result_line = line
    
    return result_line
