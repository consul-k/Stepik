/*

Найдите сумму  всех целых чисел от 1 до n включительно и верните из функции результат.

Sample Input 1:

8

Sample Output 1:

36

Sample Input 2:

2

Sample Output 2:

3

*/

function testCycle(n) {
  let x = 0;
  for (let i = 0; i <= n; i++){
      x+=i;
  }
  return x;
}

let n = Number(prompt())
console.log(testCycle(n))
