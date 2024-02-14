/*

Напишите программу, которая запрашивает у пользователя два набора из двух чисел и объявляет две функции: findMax и compareMax. 
Функция findMax принимает два числа как параметры и возвращает большее из них. 
Функция compareMax принимает результаты нахождения максимума из двух наборов чисел как параметры и выводит сообщение о том, какое число больше.

Sample Input 1:

5
12
60
30

Sample Output 1:

Максимальное число второго набора больше

Sample Input 2:

5
4
3
2

Sample Output 2:

Максимальное число первого набора больше

Sample Input 3:

4
9
9
3

Sample Output 3:

Максимальные числа наборов равны

Sample Input 4:

5
4
7
8

Sample Output 4:

Максимальное число второго набора больше

*/

let a1 = Number(prompt());
let a2 = Number(prompt());
let b1 = Number(prompt());
let b2 = Number(prompt());

function findMax(a,b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

function compareMax(a,b) {
    if (a > b) {
        console.log('Максимальное число первого набора больше');
    } else if (b > a) {
        console.log('Максимальное число второго набора больше');
    } else {
        console.log('Максимальные числа наборов равны');
    }
}

let a_set = findMax(a1, a2);
let b_set = findMax(b1, b2);

compareMax(a_set, b_set);
