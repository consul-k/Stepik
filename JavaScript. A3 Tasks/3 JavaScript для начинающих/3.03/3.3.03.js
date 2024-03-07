/*

Даны числа a и b. Выведите строку с числами от а до b, разделенных пробелами. Известно, что b больше a.

Sample Input 1:

5 6

Sample Output 1:

5 6

Sample Input 2:

9 16

Sample Output 2:

9 10 11 12 13 14 15 16

*/

function testCycle(a, b) {
  let x = [];
  for (let i = a; i <= b; i++) {
      x.push(i)
  }
  return x.join(' ');
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testCycle(a, b))
