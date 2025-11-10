translit_map = {
    'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}

def clean_text(chars):
    def decorator(func):
        def wrapper(text):
            result = func(text)
            cleaned = []
            for char in result:
                if char in chars:
                    if not cleaned or cleaned[-1] != '+':
                        cleaned.append('+')
                else:
                    cleaned.append(char)
            return ''.join(cleaned)
        return wrapper
    return decorator

@clean_text("?!:;,. ")
def transliterate(text):
    text = text.lower()
    result = []
    for char in text:
        if char in translit_map:
            result.append(translit_map[char])
        else:
            result.append(char)
    return ''.join(result)
