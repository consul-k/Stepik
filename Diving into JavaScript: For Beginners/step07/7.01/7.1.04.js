/*

Перед вами программа, которая принимает название товара, цену товара за штуку и количество товара и выводит сообщение в определенном формате 
с помощью функции calculateTotal с тремя параметрами. Напишите функцию calculateTotal. Используйте интерполяцию.

Sample Input 1:

Майка
300
6

Sample Output 1:

Вы выбрали 6 товаров "Майка" по цене 300 рублей за штуку. Итого: 1800 рублей.

Sample Input 2:

Футболка
200
3

Sample Output 2:

Вы выбрали 3 товаров "Футболка" по цене 200 рублей за штуку. Итого: 600 рублей.

*/

const itemName = prompt();
const itemPrice = Number(prompt());
const quantity = Number(prompt());

function calculateTotal(n,p,q) {
    return `Вы выбрали ${q} товаров \"${n}\" по цене ${p} рублей за штуку. Итого: ${q*p} рублей.`;
};

const message = calculateTotal(itemName, itemPrice, quantity);
console.log(message);
