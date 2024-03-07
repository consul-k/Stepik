/*

Вписать в указанное место код, который будет присваивать переменной "х" значение суммы переменных "a" и "b" - в случае если  a < b, 
разность "a" и "b" - в случае если  a > b, и их произведение  в остальных случаях.

Sample Input:

2 5

Sample Output:

7

*/

function testIf(a, b) {
    let x;
    if (a < b) {
        x = a + b;
    } else if (a > b){
        x = a - b;
    } else {
        x = a * b;
    }
    return x;
}

let [a, b] = prompt().split(' ').map(Number)
console.log(testIf(a, b))
