/*

Напишите программу, которая запрашивает у пользователя площадь основания S и высоту h, 
затем позволяет выбрать для какой фигуры найти объем: для цилиндра или для конуса. 
Затем объявляются две стрелочные функции: calculateCylinderVolume и calculateConeVolume, каждая из которых принимает параметры фигуры и возвращает объем. 

Объем цилиндра = площадь основания * высота

Объем конуса = 1/3 * площадь основания * высота

Sample Input 1:

8
6
цилиндр

Sample Output 1:

Объем цилиндра: 48

Sample Input 2:

9
9
конус

Sample Output 2:

Объем конуса: 27

Sample Input 3:

2
3
конус

Sample Output 3:

Объем конуса: 2

*/

let S = Number(prompt());
let h = Number(prompt());
let figure = prompt();

let c = (S,h) => S * h;
let k = (S,h) => 1/3 * S * h; 

if (figure === 'цилиндр') {
    let result = c(S,h);
    console.log('Объем цилиндра:', result);
} else if (figure === 'конус') {
    let result = k(S,h);
    console.log('Объем конуса:', result);
}
