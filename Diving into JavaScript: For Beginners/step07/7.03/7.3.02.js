/*

Напишите программу, которая запрашивает у пользователя строку, а затем выводит на экран последние два символа этой строки. 
Если строка состоит из меньше, чем 2 символов, выведите сообщение о том, что строка слишком короткая

Sample Input 1:

JavaScript

Sample Output 1:

pt

Sample Input 2:

Карта

Sample Output 2:

та

Sample Input 3:

f

Sample Output 3:

Введенная строка слишком короткая

*/

let str = prompt();
if (str.length > 2) {
console.log(str.slice(-2));
} else {
console.log('Введенная строка слишком короткая');
}
