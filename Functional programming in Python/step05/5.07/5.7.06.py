def aggregation(func, sequence):
    if len(sequence) < 2:
        return []

    result = []
    agg = func(sequence[0], sequence[1])
    result.append(agg)

    for item in sequence[2:]:
        agg = func(agg, item)
        result.append(agg)

    return result
