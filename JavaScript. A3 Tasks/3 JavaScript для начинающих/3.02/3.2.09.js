/*

В этом задании в нашу функцию передается угол в градусах. Вам нужно вернуть из функции значение его синуса. 
Не забывайте, что тригонометрические функции в JavaScript принимают аргументы только в радианах!

Sample Input:

348

Sample Output:

-0.20791169081775987

*/

function testMath(a) {
    let rad = a * Math.PI/180;
    return Math.sin(rad);
}

let a = Number(prompt())
console.log(testMath(a))
