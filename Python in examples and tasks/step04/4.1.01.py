'''

Семья из трех человек планирует поехать отдыхать из города А в город B. Можно полететь самолетом, а можно – на своей машине.

Билет на самолет на одного человека стоит k рублей туда и обратно. Автомобиль расходует 12 литров бензина на 100 км, 
а цена бензина –  p рублей за 1 литр. Расстояние от города А до В -  s км. Сколько рублей придется заплатить 
за самую дешевую поездку на троих туда и обратно?

Входные данные:

    стоимость билета на самолет (вещественное число);
    цена бензина (вещественное число);
    расстояние от города А до города В (вещественное число).

Выходные данные:

    сумма самой дешевой поездки (вещественное число) или '"error", если введены ошибочные данные.

Результат округлить до двух знаков после запятой (использовать функцию round()).

Sample Input 1:

-5
60
0

Sample Output 1:

error

Sample Input 2:

4500.89
45
1800

Sample Output 2:

13502.67

Sample Input 3:

5556.7
47.5
500

Sample Output 3:

5700.0

'''

def vacation_cost(ticket_price, gas_price, distance):
    flight_cost = 3 * ticket_price
    drive_distance = distance * 2  # Туда и обратно
    gas_consumption = drive_distance * 0.12  # 12 литров на 100 км
    drive_cost = gas_consumption * gas_price

    if flight_cost < 0 or gas_price < 0 or distance < 0:
        return "error"

    min_cost = min(flight_cost, drive_cost)
    return round(min_cost, 2)

k = float(input())
p = float(input())
s = float(input())

cost = vacation_cost(k, p, s)
print(cost)
