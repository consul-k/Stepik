def replace(text, old, new=''):
    new_text = ''
    for i in range(len(text)):
        if text[i] == old:
            new_text += new
        else:
            new_text += text[i]
    return new_text
