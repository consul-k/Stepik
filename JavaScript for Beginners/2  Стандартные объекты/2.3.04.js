/*

В этом задании в нашу функцию testStr передаются две строки. Вам нужно вернуть индекс позиции, с которой начинается вхождение второй строки в первую. 
Верните -1, если второй строки нет в первой.

Sample Input 1:

This is a test string
test

Sample Output 1:

10

Sample Input 2:

This is a test string for testing
test

Sample Output 2:

10

*/

function testStr(a, b) {
    return a.indexOf(b);
}
