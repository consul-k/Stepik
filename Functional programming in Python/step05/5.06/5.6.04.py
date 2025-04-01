def double_odd_numbers(numbers):
    def is_odd(n):
        return n%2 != 0
    def double(n):
        return n*2


    return [double(num) for num in numbers if is_odd(num)]
