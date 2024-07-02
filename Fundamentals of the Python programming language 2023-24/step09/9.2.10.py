def combine(goods, prices):
    zipped = list(zip(prices, goods))
    zipped.sort()
    return zipped
