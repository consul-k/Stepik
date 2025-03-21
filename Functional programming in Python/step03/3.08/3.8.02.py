def truncate_sentences(n, *text):
    for line in text:
        print(line[:n])
