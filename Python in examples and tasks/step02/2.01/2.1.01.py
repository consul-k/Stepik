'''

Вы положили некоторую сумму x в банк на n месяцев под k% годовых с капитализацией процентов. 
Расчет итоговой суммы осуществляется по формуле:

s=x⋅(1+k12⋅100)n
s=x⋅(1+12⋅100k​)nПосчитать прибыль от вложения (разницу между конечной и исходной суммой), результат округлить до целого.

Реализовать задачу на основе предложенного шаблона. Проверку входных данных не делать.

Входные данные:

    сумма вклада x руб;
    процент k;
    количество месяцев n.

Выходные данные:

    прибыль от вложения, округленная до целого числа.

Пояснение:

Для округления выходных данных использовать round().

Sample Input 1:

51800
5.83
22

Sample Output 1:

5828

Sample Input 2:

73600
7.52
16

Sample Output 2:

7737

'''

def compute_income(deposit, interest_rate, amount_months):
    income_deposit = (1 + interest_rate / (100*12) ) ** amount_months * deposit
    income_total = income_deposit - deposit
    return income_total


x = float(input())

k = float(input())

n = int(input())

# вычислить прибыль с помощью функции

s = compute_income(x,k,n)
print(round(s))
