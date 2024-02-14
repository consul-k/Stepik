/*

Напишите программу, которая запрашивает у пользователя три числа и объявляет функцию,
которая принимает три числа как параметры и возвращает их среднее арифметическое. 
Выведите удвоенное значение среднего арифметического.

Sample Input 1:

1
2
3

Sample Output 1:

4

Sample Input 2:

3
3
3

Sample Output 2:

6

Sample Input 3:

7
8
9

Sample Output 3:

16

*/

let a = Number(prompt());
let b = Number(prompt());
let c = Number(prompt());

function s(a,b,c) {
    return (a + b + c) / 3;
}

let result = s(a,b,c);
console.log(result*2);
