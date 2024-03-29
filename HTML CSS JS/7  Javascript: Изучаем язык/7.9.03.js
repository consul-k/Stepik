/*

  На ввод поступает строка (количество лет), необходимо конвертировать его в число.

    Если возраст больше, либо равен 18, вывести "Доступ разрешен", если меньше, то "Доступ запрещен".
    Входные данные

    В одной строке вводятся число (количество лет).
    Выходные данные

    Либо "Доступ разрешен", либо "Доступ запрещен".

Sample Input:

18

Sample Output:

Доступ разрешен

*/

let x = Number(prompt());
let res = (x > 18 || x === 18) ? "Доступ разрешен" : "Доступ запрещен";
console.log(res);
