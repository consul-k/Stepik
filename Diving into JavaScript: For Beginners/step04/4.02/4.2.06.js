/*

Напишите программу, которая будет запрашивать у пользователя число . 
Затем программа должна вычислить и вывести сумму всех нечетных чисел от 1 до введенного числа включительно.

Sample Input 1:

7

Sample Output 1:

Сумма нечетных чисел от 1 до 7 равна 16

Sample Input 2:

5

Sample Output 2:

Сумма нечетных чисел от 1 до 5 равна 9

Sample Input 3:

9

Sample Output 3:

Сумма нечетных чисел от 1 до 9 равна 25

*/

let n = Number(prompt());
let sum = 0;

for (let i = 1; i <= n; i++) {
    if (i%2!=0) {
        sum+=i;
    }
}
console.log('Сумма нечетных чисел от 1 до',n,'равна',sum);
