def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    filtered = filter(lambda x: x % 3 == 0, nums)
    mapped = map(lambda x: x * 3, filtered)
    
    return tuple(mapped)
