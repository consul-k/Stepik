n = int(input())  # количество товаров
first = [int(input()) for _ in range(n)]       # цены из "Шестёрочки"
second = [int(input()) for _ in range(n)]      # цены из "Пересечения"

# Создаём список минимальных цен
result = [min(first[i], second[i]) for i in range(n)]

# Выводим через пробел
print(*result)
