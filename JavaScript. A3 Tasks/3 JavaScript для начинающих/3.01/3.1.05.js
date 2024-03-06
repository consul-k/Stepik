/*

Вписать в указанное место код, который будет присваивать переменной "х" значение суммы переменных "a" и "b" в случае 
если  a > b или их произведение в остальных случаях.

Sample Input:

5 4

Sample Output:

9

*/

function testIf(a, b) {
    let x;
    if (a > b) {
        x = a + b;
    } else {
        x = a * b;
    }
    return x;
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testIf(a, b))
