/*

В этом задании вам необходимо выполнить возведение переменной a в степень b и возврат значения из функции.

Sample Input:

5 3

Sample Output:

125

*/

function testMath(a, b) {
  return Math.pow(a,b);
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testMath(a, b))
