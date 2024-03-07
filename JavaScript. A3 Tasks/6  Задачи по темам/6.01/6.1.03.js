/*

Дана величина угла в градусах -- положительное натуральное число.

Переведите величину угла в радианы по формуле radians=degrees⋅2π360radians=degrees⋅3602π​

Sample Input 1:

180

Sample Output 1:

3.1416

Sample Input 2:

57

Sample Output 2:

0.9948

*/

let degrees = Number(prompt());
let radians = degrees * (2*Math.PI/360);
console.log(radians.toFixed(4));
