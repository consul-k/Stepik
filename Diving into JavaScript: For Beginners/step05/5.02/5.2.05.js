/*

Напишите программу, которая запрашивает у пользователя два числа и операцию (+, -, * или /). 
Затем объявите функцию, которая принимает два числа и операцию как параметры и выводит на экран результат выполнения выбранной операции. 
Если пользователь ввел неверный оператор, программа выводит "Неверный оператор"

Sample Input 1:

5
2
+

Sample Output 1:

7

Sample Input 2:

7
7
/

Sample Output 2:

1

Sample Input 3:

8
5
=

Sample Output 3:

Неверный оператор

Sample Input 4:

8
9
*

Sample Output 4:

72

*/

let a = Number(prompt());
let b = Number(prompt());
let s = prompt();

function operation(a, b, s) {
    if (s === '+') {
    console.log(a + b);
  } else if (s === '-') {
    console.log(a - b);
  }  else if (s === '*') {
    console.log(a * b);
  } else if (s === '/') {
    console.log(a / b);
  } else {
    console.log('Неверный оператор');
  }
}

operation(a, b, s);
