/*

Напишите программу, которая запрашивает три цифры и выводит число из цифр в том же порядке, что и при вводе.

Sample Input 1:

1
2
3

Sample Output 1:

123

Sample Input 2:

0
2
3

Sample Output 2:

23

*/

let A = prompt();
let B = prompt();
let C = prompt();

let res = A + B + C;
console.log(Number(res));
