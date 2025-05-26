def count_calls():
    def inner():
        inner.total_calls += 1
        return inner.total_calls

    inner.total_calls = 0
    return inner
