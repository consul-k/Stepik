/*

Попросите пользователя ввести строку. Если длина строки меньше 5 символов, добавьте к строке "!" и выведите результат, 
иначе добавьте к строке "?" и также выведите результат.

Sample Input 1:

Братва

Sample Output 1:

Братва?

Sample Input 2:

Брат

Sample Output 2:

Брат!

*/

let str = prompt();

if (str.length < 5) {
    console.log(str+'!');
} else {
    console.log(str+'?');
}
