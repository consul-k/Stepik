def func(*names):
    if len(names) == 1:
        return f"Привет, {names[0]}!"
    else:
        last_name = names[-1]
        other_names = ", ".join(names[:-1])
        return f"Привет, {other_names} и {last_name}!"
