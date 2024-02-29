/*

Напишите функцию для вычисления среднего арифметического массива arr.

    Функция должна вернуть среднее арифметическое, округленное до целого.

Sample Input:

1, 6, 3, 5, 1

Sample Output:

3

*/

function avg(arr){
    let sum = arr.reduce((a, b) => a + b, 0);
    return Math.round(sum / arr.length);
}
