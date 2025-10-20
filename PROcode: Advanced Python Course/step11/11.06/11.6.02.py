def headline_formatter():
    def wrap(text: str) -> str:
        return f"<h2>{text}</h2>"
    return wrap
