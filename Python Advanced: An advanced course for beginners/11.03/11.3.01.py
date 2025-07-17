def count_messages(messages):
    count = 0
    for item in messages:
        if isinstance(item, str):
            count += 1
        elif isinstance(item, list):
            count += count_messages(item)
    return count
