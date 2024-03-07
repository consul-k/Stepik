/*

В этом задании в нашу функцию testDateTime передаются две строки вида "03 November 2017 04:17".
Вам нужно превратить строки в даты, сравнить их. Для той, что больше получить день недели и вернуть его из функции.

Название дня недели должно быть по-русски, с большой буквы, например: "Понедельник".

Sample Input 1:

27 November 1909 20:32
22 September 1909 13:17

Sample Output 1:

Суббота

Sample Input 2:

01 December 1909 03:17
24 August 1909 13:09

Sample Output 2:

Среда

*/

function testDateTime(a, b) {
    var n = new Date(a);
    var m = new Date(b);
    var days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
    if (n > m) {
        return days[n.getDay()];
    }
    else {
        return days[m.getDay()];
    }
    
}

let a = prompt()
let b = prompt()
console.log(testDateTime(a, b))
