/*

Есть некоторый рабочий код, который закомментирован.
Нужно убрать все комментарии, чтобы код заработал, и нажать кнопку Отправить.

*/

function testComment(a, b) {
    let x;
    x = a * b;
   
    return x;
}

let a = Number(prompt()) 
let b = Number(prompt())
console.log(testComment(a, b))
