/*

В этом задании в нашу функцию testRegExp первым параметром передается случайная строка(переменная s), 
а вторым - случайная подстрока(переменная sub_s), которую нужно использовать в качестве шаблона регулярного выражения. 
Вам нужно вернуть из функции строку, в которой будут перечислены через запятую все совпадения шаблона с первой строкой.


Sample Input 1:

Insoimpossibleaiderppearideranceconsiiderderidereiderdmiiderderr
ider

Sample Output 1:

ider,ider,ider,ider,ider,ider

Sample Input 2:

Mrdispodisidingdicontinueditoffendingarradinginginwe
di

Sample Output 2:

di,di,di,di,di,di,di

*/

function testRegExp(s, sub_s) {
    let res = s.matchAll(sub_s);
    return Array.from(res).join(',');
}

let s = prompt()
let sub_s = prompt()
console.log(testRegExp(s, sub_s))
