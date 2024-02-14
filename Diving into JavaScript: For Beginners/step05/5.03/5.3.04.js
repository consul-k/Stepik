/*

Напишите программу, которая запрашивает у пользователя длины трех сторон треугольника и объявляет функцию checkTriangleExistence, 
которая принимает длины сторон в качестве параметров и возвращает сообщение о том, существует ли треугольник с такими сторонами или нет.

Чтобы проверить треугольник на существование, нужно сравнить каждую сторону с суммой двух других. 
Если хотя бы в одном случае сторона окажется больше либо равна сумме двух других, то треугольника с такими сторонами не существует.

Sample Input 1:

4
2
3

Sample Output 1:

Треугольник существует

Sample Input 2:

3
4
5

Sample Output 2:

Треугольник существует

Sample Input 3:

9
3
5

Sample Output 3:

Треугольник не существует

Sample Input 4:

2
5
1

Sample Output 4:

Треугольник не существует

Sample Input 5:

7
0
12

Sample Output 5:

Треугольник не существует

*/

let a = Number(prompt());
let b = Number(prompt());
let c = Number(prompt());

function checkTriangleExistence(a, b, c) {
    if (a >= b+c || b >= c + a || c >= a + b) {
        return 'Треугольник не существует';
    } else {
        return 'Треугольник существует';
    }
}

let result = checkTriangleExistence(a, b, c);
console.log(result);
