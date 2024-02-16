/*

Пользователь вводит возраст. Напишите программу, которая проверяет, я
вляется ли введенное значение числом и находится ли оно в диапазоне от 18 до 65 лет включительно. 
Если введенное значение не является числом, программа выводит сообщение об ошибке. 
Если число не попадает в диапазон выводится "Доступ запрещен", в иных случаях выводится сообщение "Доступ разрешен".

Sample Input 1:

call me babydoll

Sample Output 1:

Ошибка: Введите ваш возраст

Sample Input 2:

97

Sample Output 2:

Доступ запрещен

Sample Input 3:

18

Sample Output 3:

Доступ разрешен

Sample Input 4:

62

Sample Output 4:

Доступ разрешен

*/

let age = prompt();

if (isNaN(age)) {
    console.log('Ошибка: Введите ваш возраст');
} else {
    if (parseInt(age) < 18 || parseInt(age) > 65) {
        console.log('Доступ запрещен');
    } else {
        console.log('Доступ разрешен');
    }
}
