/*

Напишите программу, которая запрашивает у пользователя два набора из двух чисел и объявляет две функции: calculateAverage и compareAverages. 
Функция calculateAverage принимает два числа как параметры и возвращает их среднее арифметическое. 
Функция compareAverages принимает результаты средних значений из двух наборов чисел как параметры и выводит сообщение о том, 
какое среднее значение больше.

Sample Input 1:

7
5
9
3

Sample Output 1:

Средние значения наборов равны

Sample Input 2:

8
6
9
6

Sample Output 2:

Среднее значение второго набора больше

Sample Input 3:

13
46
2
5

Sample Output 3:

Среднее значение первого набора больше

Sample Input 4:

15
65
2
1

Sample Output 4:

Среднее значение первого набора больше

*/

let a1 = Number(prompt());
let a2 = Number(prompt());
let b1 = Number(prompt());
let b2 = Number(prompt());

function calculateAverage(a,b) {
    return (a + b) / 2;
}

function compareAverages(a,b) {
    if (a > b) {
        console.log('Среднее значение первого набора больше');
    } else if (b > a) {
        console.log('Среднее значение второго набора больше');
    } else {
        console.log('Средние значения наборов равны');
    }
}

let a_set = calculateAverage(a1, a2);
let b_set = calculateAverage(b1, b2);

compareAverages(a_set, b_set);
