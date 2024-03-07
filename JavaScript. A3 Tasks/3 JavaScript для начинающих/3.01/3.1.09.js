/*

Вычислить сумму всех четных чисел, встречающихся в ряду от 1 до числа (включительно), передаваемого в нашу функцию (переменная "а").

Sample Input:

3

Sample Output:

2

*/

function testWhile(a) {
    let x = 0;
    let s = 1;
    while (s <= a) {
        if (s%2===0) {
            x+=s;
        }
        s++;
    }
    return x;
    return x;
}

let a = Number(prompt())
console.log(testWhile(a))
