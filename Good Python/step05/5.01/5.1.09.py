n = int(input())
for _ in range(n):
    grade = int(input())
    if grade > 100:
        print("Сакура взломала тестирующую систему")
    elif grade >= 80 and grade <= 100:
        print("Сакура списала с Тоши")
    elif grade >= 60 and grade < 80:
        print("Сакура списала с Мику")
    elif grade < 60 and grade >= 0:
        print("Сакура писала тест честно")
    else:
        print("Тоши взломал тестирующую систему")
