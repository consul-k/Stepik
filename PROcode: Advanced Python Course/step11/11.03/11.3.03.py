def flatten_data(d, a=None):
    if a is None:
        a = []
    for item in d:
        if isinstance(item, list):
            flatten_data(item, a)
        else:
            a.append(item)
    return a
