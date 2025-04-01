def wrap_increment(value):
    # определите вложенную функцию _inc
    def _inc(value):
        return value+1
    
    return _inc(value)
