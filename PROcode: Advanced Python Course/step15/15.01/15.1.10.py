def analyze_battle(text):
    words = text.split()
    
    total_words = len(words)
    
    unique_words = len(set(words))
    
    word_count = {}
    most_frequent_word = None
    max_count = 0
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_frequent_word = word
    
    return (total_words, unique_words, most_frequent_word)
