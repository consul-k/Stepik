/*

Перепишите код из предыдущего шага, используя стрелочные функции.

Sample Input 1:

5

Sample Output 1:

false

Sample Input 2:

2

Sample Output 2:

true

Sample Input 3:

11

Sample Output 3:

false

*/

let a = Number(prompt());
let isEven = num => num % 2 === 0;
console.log(isEven(a));
