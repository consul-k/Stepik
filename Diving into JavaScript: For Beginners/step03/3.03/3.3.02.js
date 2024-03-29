/*

Создайте программу для вычисления стоимости доставки товара в зависимости от его веса. 
Запросите у пользователя вес товара. Используя тернарный оператор, 
определите стоимость доставки в зависимости от введенного веса:

    Если вес товара менее или равен 5 кг, стоимость - 200 рублей.
    Если вес товара больше 5 кг, стоимость - 350 рублей.

Sample Input 1:

4

Sample Output 1:

Стоимость доставки: 200 рублей

Sample Input 2:

7

Sample Output 2:

Стоимость доставки: 350 рублей

Sample Input 3:

12

Sample Output 3:

Стоимость доставки: 350 рублей

*/

let w = Number(prompt());

let price = (w <= 5) ? 200 : 350;

console.log('Стоимость доставки: ' + price + ' рублей');
