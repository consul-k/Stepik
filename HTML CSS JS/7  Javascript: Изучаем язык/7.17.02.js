/*

   На вход подается несколько чисел, разделенных пробелом.

    Вам нужно, используя стрелочную функцию, создать и вывести массив, состоящий из этих чисел, но с противоположным знаком.

Sample Input:

1 2 -3 4 5

Sample Output:

[ -1, -2, 3, -4, -5 ]

*/

let arr = prompt().split(' ').map(Number);
let revNums = arr.map(number=>-number);
console.log(revNums);
