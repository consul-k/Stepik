def aggregation(func, sequence):
    if len(sequence) < 2:
        raise ValueError("Sequence must contain at least two elements")

    result = func(sequence[0], sequence[1])

    for item in sequence[2:]:
        result = func(result, item)

    return result
