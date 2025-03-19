def is_only_one_positive(*args):
    res = [i for i in args if i > 0]
    if res and len(res) == 1:
        return True
    else:
        return False
