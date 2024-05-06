def func(*args):
    prod = ['молоко', 'мясо', 'бананы', 'курица', 'рыба', 'йогурт', 'масло', 'солёные огурчики']
    res = [arg for arg in args if isinstance(arg, str) and arg in prod]
    res.sort()
    return "\n".join(f"{i+1}. {prod}" for i, prod in enumerate(res))
