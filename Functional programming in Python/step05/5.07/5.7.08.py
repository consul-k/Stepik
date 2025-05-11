def aggregation(func, sequence, initial=None):
    if not sequence and initial is None:
        raise ValueError("Sequence must contain at least two elements or an initial value")

    if initial is not None:
        result = initial
        for item in sequence:
            result = func(result, item)
    else:
        if len(sequence) < 2:
            raise ValueError("Sequence must contain at least two elements")
        result = func(sequence[0], sequence[1])
        for item in sequence[2:]:
            result = func(result, item)

    return result
