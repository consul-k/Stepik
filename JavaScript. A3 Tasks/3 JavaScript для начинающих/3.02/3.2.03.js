/*


В этом задании в нашу функцию testStr первым параметром передается строка (переменная str), 
а вторым - число (переменная n) . Вам нужно вернуть из функции символ строки , порядковый номер которого указан в переданном в функцию числе.

Подсказка: порядковый номер не равен индексу символа в строке.

Sample Input:

Veryyeladygirlthemgoodmemake
24

Sample Output:

e

*/

function testStr(str, n) {
    return str[n-1];
}

let str = prompt()
let n = Number(prompt())
console.log(testStr(str, n))
