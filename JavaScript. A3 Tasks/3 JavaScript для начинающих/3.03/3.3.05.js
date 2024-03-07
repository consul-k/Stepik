/*

Даны числа a и b. Выведите строку с числами от большего числа до меньшего. 
Известно, что и a и b больше либо равно 1, но неизвестно, какое из них больше.

Sample Input 1:

8 7

Sample Output 1:

8 7

Sample Input 2:

11 14

Sample Output 2:

14 13 12 11

Sample Input 3:

13 3

Sample Output 3:

13 12 11 10 9 8 7 6 5 4 3

*/

function testCycle(a, b) {
  let x = [];
  if (a===b) {
      return a;
  }
  if (a > b) {
      for (let i = a; i >= b; i--) {
          x.push(i)
      }
  } if (b > a) {
      for (let i = b; i >= a; i--) {
          x.push(i)
      }
  }
  return x.join(' ');
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testCycle(a, b))
