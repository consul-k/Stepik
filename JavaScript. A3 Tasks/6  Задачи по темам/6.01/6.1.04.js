/*

На автозаправке клиент отдал кассиру xx рублей и попросил залить бензин до полного бака. 
Цена бензина yy рублей за литр. Клиент получил zz рубля сдачи. Сколько литров бензина было залито в бак?

Даны переменные x, y, z на отдельных строках.

https://ege.sdamgia.ru/problem?id=282848

Sample Input:

2000
53
72

Sample Output:

36

*/

let x = Number(prompt());  // x - дано рублей
let y = Number(prompt());  // y - цена бензина
let z = Number(prompt());  // z - сдача

console.log(Math.round((x-z)/y));
