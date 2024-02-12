/*

Напишите программу, которая по введенным от пользователя длинам сторон треугольника определяет его вид:
равносторонний, равнобедренный или разносторонний.

    Если все три стороны равны, то это равносторонний треугольник.
    Если любые две из трех сторон равны, то это равнобедренный треугольник.
    Если ни одно из условий выше не выполняется, то это разносторонний треугольник.

Sample Input 1:

8
8
8

Sample Output 1:

Равносторонний

Sample Input 2:

6
5
3

Sample Output 2:

Разносторонний

Sample Input 3:

2
2
3

Sample Output 3:

Равнобедренный

Sample Input 4:

5
4
4

Sample Output 4:

Равнобедренный

Sample Input 5:

9
6
9

Sample Output 5:

Равнобедренный

*/

let a = Number(prompt());
let b = Number(prompt());
let c = Number(prompt());

if (a === b && b === c && c === a) {
    console.log('Равносторонний');
}
else if (a === b || a === c || b === c) {
    console.log('Равнобедренный');
}
else {
    console.log('Разносторонний');
}
