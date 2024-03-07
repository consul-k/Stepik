/*

В этом задании в нашу функцию передаются 4 числа. Вам необходимо вычислить результат деления большего из этих чисел на меньшее, 
и округлив до ближайшего меньшего целого вернуть из функции.

Sample Input:

7 4 8 9

Sample Output:

2

*/

function testMath(a, b, c, d) {
    let min_n = Math.min(a,b,c,d);
    let max_n = Math.max(a,b,c,d);
    let res = Math.floor(max_n/min_n);
    return res;
}

let [a, b, c, d] = prompt().split(' ').map(Number)
console.log(testMath(a, b, c, d))
