/*

Напишите программу, которая запрашивает ввод строки. Если эта строка содержит символ "д" или символ "н", 
то программа выводит всю строку в верхнем регистре, а иначе выводится строка в нижнем регистре.

Sample Input 1:

ода

Sample Output 1:

ОДА

Sample Input 2:

Дом 

Sample Output 2:

дом

Sample Input 3:

Савелий Крамаров

Sample Output 3:

савелий крамаров

Sample Input 4:

Мона Лиза

Sample Output 4:

МОНА ЛИЗА

*/

let str = prompt();

if (str.includes("д") || str.includes("н")) {
    console.log(str.toUpperCase());
} else {
    console.log(str.toLowerCase());
}
