/*

В этом задании в нашу функцию testArray передаются два массива случайной длины заполненные случайными числами. 
Вам нужно сосчитать сумму всех элементов обоих массивов и возвратить ее из функции.

Sample Input:

[0, 1, 5, 3]  [3]

Sample Output:

12

*/

function testArray(a, b) {
    let sum = 0;
    a = a.concat(b);
    for (num of a) {
        sum+=num;
    }
    return sum;
}
