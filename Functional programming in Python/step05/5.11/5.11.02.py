def limit_query(func):
    count = 0  # переменная для подсчета вызовов

    def add(*args, **kwargs):
        nonlocal count
        if count < 3:
            count += 1
            return func(*args, **kwargs)
        else:
            print("Лимит вызовов закончен, все 3 попытки израсходованы")
            return None

    return add
