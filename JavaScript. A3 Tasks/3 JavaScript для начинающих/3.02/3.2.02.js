/*

В этом задании в нашу функцию testStr передаются две строки. Вам нужно вернуть из функции их суммарную длину.

Sample Input:

Hello
World!

Sample Output:

11

*/

function testStr(a, b) {
    return a.length + b.length;
}

let a = prompt()
let b = prompt()
console.log(testStr(a, b))
