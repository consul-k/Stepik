/*

Напишите программу, которая запрашивает у пользователя два числа и сравнивает их. 
Затем объявите функцию, которая принимает два числа как параметры и выводит на экран сообщение о том, какое число больше.

Sample Input 1:

7
6

Sample Output 1:

7 больше, чем 6

Sample Input 2:

9
10

Sample Output 2:

10 больше, чем 9

Sample Input 3:

5
5

Sample Output 3:

5 равно 5

Sample Input 4:

36
45

Sample Output 4:

45 больше, чем 36

*/

let a = Number(prompt());
let b = Number(prompt());

function comp(a, b) {
    if (a > b) {
    console.log(a, 'больше, чем', b);
  } else if (b > a) {
    console.log(b, 'больше, чем', a);
  } else {
    console.log(a, 'равно', b);
  }
}

comp(a,b);
