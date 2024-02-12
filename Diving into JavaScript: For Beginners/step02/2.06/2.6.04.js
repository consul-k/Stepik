/*

Запросите у пользователя число a, а затем число b. 
Проверьте является ли число а меньше числа b и присвойте результат проверки константе isLess. 
Выведите значение константы isLess.

Sample Input 1:

8
11

Sample Output 1:

true

Sample Input 2:

7
5

Sample Output 2:

false

Sample Input 3:

6
6

Sample Output 3:

false

*/

let a = Number(prompt());
let b = Number(prompt());

const isLess = a < b;
console.log(isLess);
