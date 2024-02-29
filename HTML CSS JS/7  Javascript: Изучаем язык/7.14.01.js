/*

  Представьте, что вы разрабатываете программу для автоматизации процесса приема заказов в ресторане. 
  Задача состоит в том, чтобы проверить, есть ли блюдо, которое заказал клиент, в меню ресторана. 
  Если блюдо есть в меню, то программа должна добавить его в заказ и вывести сообщение о том, что блюдо успешно добавлено. 
  Если блюда нет в меню, то программа должна отказать в добавлении и вывести сообщение об ошибке.

Меню:

    Тар-тар из говядины с битыми огурцами
    Мясные деликатесы
    Цезарь с цыпленком
    Спагетти Карбонара
    Сырная тарелка

Входные данные

    В одной строке вводятся название блюда.
Выходные данные

    Либо "Заказ добавлен", либо "Нет такого блюда в меню".

Sample Input 1:

Тар-тар из говядины с битыми огурцами

Sample Output 1:

Заказ добавлен

Sample Input 2:

Сырная тарелка

Sample Output 2:

Заказ добавлен

*/

let a = prompt("Введите блюдо");
switch (a) {
    case "Тар-тар из говядины с битыми огурцами":
        console.log('Заказ добавлен');
        break;
    case "Мясные деликатесы":
        console.log( 'Заказ добавлен' );
        break;
    case "Цезарь с цыпленком":
        console.log( 'Заказ добавлен' );
        break;
    case "Спагетти Карбонара":
        console.log( 'Заказ добавлен' );
        break;
    case "Сырная тарелка":        
        console.log( 'Заказ добавлен' );
        break;
    default:
        console.log( "Нет такого блюда в меню" );
}
