from typing import List, Optional

def get_first_repeated_word(words: List[str]) -> Optional[str]:
    'Находит первый дубль в списке'
    seen = set()
    
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    
    return None
