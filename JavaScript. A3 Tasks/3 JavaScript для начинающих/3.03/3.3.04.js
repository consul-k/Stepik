/*

Даны числа a и b. Выведите строку с числами между а и b включая границы, отсортированными по возрастанию. 
Неизвестно, какое из чисел больше, но известно, что и a и b больше 0.

Sample Input 1:

8 1

Sample Output 1:

1 2 3 4 5 6 7 8

Sample Input 2:

6 6

Sample Output 2:

6

Sample Input 3:

3 5

Sample Output 3:

3 4 5

*/

function testCycle(a, b) {
  let x = [];
  if (a===b) {
      return a;
  }
  if (a > b) {
      for (let i = b; i <= a; i++) {
          x.push(i)
      }
  } if (b > a) {
      for (let i = a; i <= b; i++) {
          x.push(i)
      }
  }
  return x.join(' ');
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testCycle(a, b))
