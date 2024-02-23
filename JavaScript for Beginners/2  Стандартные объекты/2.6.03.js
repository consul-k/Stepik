/*

В этом задании в нашу функцию передаются 4 числа. Вам необходимо вычислить результат деления большего из этих чисел на меньшее, 
и округлив до ближайшего меньшего целого вернуть из функции.

Sample Input:

1 4 8 8

Sample Output:

8

*/

function testMath(a, b, c, d) {
    let min_n = Math.min(a,b,c,d);
    let max_n = Math.max(a,b,c,d);
    let res = Math.floor(max_n/min_n);
    return res;
}
