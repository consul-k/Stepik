line = input()
numbers = [int(s) for s in line.split()]

# напишите ваше решение здесь
n = int(input())
numbers.sort(reverse=True)
print(numbers[n-1])
