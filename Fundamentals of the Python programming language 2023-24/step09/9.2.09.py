def min_max_avg(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    avg_num = sum(numbers) / len(numbers)
    return (min_num, max_num, avg_num)
