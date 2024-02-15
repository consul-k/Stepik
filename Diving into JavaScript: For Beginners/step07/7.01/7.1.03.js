/*

Создайте объект budget со свойствами income (доход) и expenses (расходы), значения которых вводятся пользователем и методом calculateProfit, 
который высчитывает прибыль по следующей формуле:

    Прибыль = доход - расходы

Если прибыль положительная, программа выводит значение прибыли. Если прибыль равна нулю, программа выводит сообщение о том, 
что пользователь отработал в ноль. Если прибыль отрицательна, программа выводит насколько пользователь ушел в минус. 

Используйте интерполяцию.

Sample Input 1:

15000
5000

Sample Output 1:

Ваша прибыль составляет 10000 рублей

Sample Input 2:

525200
525200

Sample Output 2:

Вы отработали в ноль

Sample Input 3:

5
130000

Sample Output 3:

Вы ушли в минус на 129995 рублей

*/

const budget = {
    calculateProfit () {
        return this.income - this.expenses
    }
};

budget.income = Number(prompt());
budget.expenses = Number(prompt());

if (budget.calculateProfit() > 0) {
    console.log(`Ваша прибыль составляет ${budget.calculateProfit()} рублей`);
} else if (budget.calculateProfit() < 0) {
    console.log(`Вы ушли в минус на ${-budget.calculateProfit()} рублей`);
} else if (budget.calculateProfit() === 0) {
    console.log('Вы отработали в ноль');
}
