/*

Перед вами та же программа, но теперь формат вывода сообщения изменен. Напишите функцию с одной инструкцией console.log(), 
в которой должны быть использованы спецсимволы.

Sample Input 1:

Футболка
200
3

Sample Output 1:

Вы выбрали "Футболка" по цене 200 рублей за штуку.
Количество: 3 шт.
Итого: 600 рублей.

Sample Input 2:

Платье
1500
2

Sample Output 2:

Вы выбрали "Платье" по цене 1500 рублей за штуку.
Количество: 2 шт.
Итого: 3000 рублей.

*/

const itemName = prompt();
const itemPrice = Number(prompt());
const quantity = Number(prompt());

function calculateTotal(n,p,q) {
    return `Вы выбрали \"${n}\" по цене ${p} рублей за штуку.\nКоличество: ${q} шт.\nИтого: ${q*p} рублей.`;
};

const message = calculateTotal(itemName, itemPrice, quantity);
console.log(message);
