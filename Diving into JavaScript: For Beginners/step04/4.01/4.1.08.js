/*

Попросите пользователя ввести число. Затем используя цикл while, 
умножайте это число на 2 до тех пор, пока оно не превысит 1000. 
Выведите на экран итоговое число и количество итераций (сколько раз вы умножили исходное число на 2).

Sample Input 1:

2

Sample Output 1:

Итоговое число: 1024
Количество итераций: 9

Sample Input 2:

5

Sample Output 2:

Итоговое число: 1280
Количество итераций: 8

Sample Input 3:

9

Sample Output 3:

Итоговое число: 1152
Количество итераций: 7

*/

let n = Number(prompt());
let count = 0;

while (n < 1000) {
    n*=2;
    count++;
}
console.log('Итоговое число:',n);
console.log('Количество итераций:',count);
