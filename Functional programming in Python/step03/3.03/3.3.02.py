def translate_to_robber_lang(text):
    new_text = ''
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for i in text:
        if i in consonants:
            new_text += i + 'o' + i
        else:
            new_text += i
    return new_text
