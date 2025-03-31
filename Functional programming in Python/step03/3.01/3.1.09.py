def is_dunder(method: str) -> bool:
    return method[:2] + method[-2:] == '_'*4 and method[2:-2].isalpha() and len(method[2:-2]) > 1
