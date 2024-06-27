def filter_prime(numbers):
    def prime(n):
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

    return [num for num in numbers if prime(num)]
