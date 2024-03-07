/*

Даны два целых числа k и n. Верните из функции строку, которая состоит из чисел n, повторяющихся k раз, разделенных пробелом. 
Известно, что и k и n больше либо равно 1.

Sample Input 1:

9 5

Sample Output 1:

5 5 5 5 5 5 5 5 5

Sample Input 2:

6 1

Sample Output 2:

1 1 1 1 1 1

*/

function testCycle(k, n) {
  let x = [];
  for (let i = 0; i < k; i++) {
      x.push(n)
  }
  return x.join(' ');
}

let [k, n] = prompt().split(' ').map(Number)
console.log(testCycle(k, n))
