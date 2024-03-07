/*

В этом задании в нашу функцию testArray передаются два массива случайной длины заполненные случайными числами. 
Вам нужно сосчитать сумму всех элементов обоих массивов и возвратить ее из функции.

Sample Input:

[8, 1, 1, 7, 4, 0]  [5, 8, 5, 4, 8]

Sample Output:

51

*/

function testArray(a, b) {
    let sum = 0;
    a = a.concat(b);
    for (num of a) {
        sum+=num;
    }
    return sum;
}

let [a, b] = prompt().split('  ').map(JSON.parse)
console.log(testArray(a, b))
