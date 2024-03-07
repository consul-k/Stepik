/*

А тут вам нужно вычислить и вернуть из функции площадь треугольника. 
Передаваемые в функцию аргументы "a" и "b" - это длины сторон, а "c" - это угол между ними в градусах.


Sample Input:

2 10 16

Sample Output:

2.7563735581699915

*/

function testMath(a, b, c) {
    let rad = c * Math.PI/180;
    S = 1/2*a*b*Math.sin(rad);
    return S
}

let [a, b, c] = prompt().split(' ').map(Number)
console.log(testMath(a, b, c))
