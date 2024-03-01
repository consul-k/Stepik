/*

Утроенное произведение

Даны два числа в переменных x, y. 

Запишите три раза подряд произведение этих чисел.

Sample Input 1:

10 
5

Sample Output 1:

505050

Sample Input 2:

80
4

Sample Output 2:

320320320

*/

// числа заданы в переменных x, y
let arr = [];

for (let i = 1; i <= 3; i++) {
    arr.push(x*y);
}
arr = arr.join('');
console.log(arr);
