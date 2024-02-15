/*

Перед вами программа, которая выводит информацию о личности в определенном формате, взяв ее из объекта, 
свойства которого вводятся пользователем. Вместо многоточия вставьте интерполированную строку правильным образом.

Sample Input 1:

Аня
19

Sample Output 1:

Имя: Аня, Возраст: 19 лет

Sample Input 2:

Саша
5

Sample Output 2:

Имя: Саша, Возраст: 5 лет

*/

const person = {};
person.name = prompt();
person.age = Number(prompt());
const info = `Имя: ${person.name}, Возраст: ${person.age} лет`;
console.log(info);
