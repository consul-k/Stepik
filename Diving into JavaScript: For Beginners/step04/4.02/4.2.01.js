/*

Перед вами программа, которая должна запрашивать у пользователя число. 
Затем программа должна вывести все четные числа от 2 до введенного числа включительно. 
Впишите вместо многоточия правильную инструкцию.

Sample Input 1:

8

Sample Output 1:

2
4
6
8

Sample Input 2:

13

Sample Output 2:

2
4
6
8
10
12

*/

let n = Number(prompt("Введите целое число:"));

for (let i = 2; i <= n; i += 2) {
  console.log(i);
}
