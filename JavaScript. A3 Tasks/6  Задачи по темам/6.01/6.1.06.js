/*

Даны две вещественные точки на прямой -- x1x1​ и x2x2​.

Найти расстояние между ними.

Sample Input:

2
5

Sample Output:

3

*/

x1 = Number(prompt());
x2 = Number(prompt());
if (x2>x1) {
    console.log(x2-x1);
} else {
    console.log(x1-x2);
