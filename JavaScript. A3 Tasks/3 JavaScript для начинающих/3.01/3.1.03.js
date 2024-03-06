/*

Вписать в указанное место код, который будет присваивать переменной "х" значение суммы переменных "a" и "b".

Указанные ниже Sample Input (образец входных данных) и Sample Output (образец выходных данных) - это пример. 
Они показывают, что при значениях переменных "a" и "b" как в Sample Input, например 2 и 8, ваш результат должен быть такой, как указано в Sample Output. 
Например, если Sample Input равен 2 и 8, то Sample Output должен быть 10, т.е. сумма первой и второй переменных.

Sample Input:

9 6

Sample Output:

15

*/

function testSum(a, b) {
    let x;
    x = a + b;
    return x;
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testSum(a, b))
