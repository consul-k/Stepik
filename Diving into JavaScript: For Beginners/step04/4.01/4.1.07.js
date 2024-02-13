/*

Напишите программу, которая будет запрашивать у пользователя целое число N. 
Затем программа должна вычислить и вывести результат возведения числа 2 в степень N. 
Реализуйте программу с помощью цикла while.

Sample Input 1:

3

Sample Output 1:

8

Sample Input 2:

4

Sample Output 2:

16

Sample Input 3:

6

Sample Output 3:

64

Sample Input 4:

8

Sample Output 4:

256

*/

let n = Number(prompt());
let two = 2;
let step = 1;

while (step < n) {
    two*=2;
    step++;
}
console.log(two);
