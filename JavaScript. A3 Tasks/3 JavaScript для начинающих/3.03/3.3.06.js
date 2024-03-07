/*

Даны числа a и b. Найдите сумму квадратов чисел между a и b включительно. Неизвестно, какое из чисел a или b больше.

Sample Input 1:

9 4

Sample Output 1:

271

Sample Input 2:

2 7

Sample Output 2:

139

*/

function testCycle(a, b) {
    let x = 0;
    for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
        x += i ** 2;
    }
    return x;
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testCycle(a, b))
