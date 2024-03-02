/*

Получите два числа из одной строки и выведите их произведение.

Sample Input:

8 11

Sample Output:

88

*/

let [a, b] = prompt().trim().split(' ').map(Number);
console.log(a*b);
