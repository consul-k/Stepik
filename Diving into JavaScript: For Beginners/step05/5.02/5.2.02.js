/*

Напишите программу, которая запрашивает у пользователя число, а затем объявите функцию, 
которая принимает это число как параметр и выводит его факториал на экран. Вызовите функцию.

Sample Input 1:

5

Sample Output 1:

120

Sample Input 2:

4

Sample Output 2:

24

Sample Input 3:

3

Sample Output 3:

6

*/

let n = Number(prompt());

function fact(n) {
    let f = 1;
    for (let i = 1; i <= n; i++) {
        f *= i;
    }
    console.log(f);
}  

fact(n);
