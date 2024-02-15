/*

Создайте объект trip с информацией о путешествии. Попросите пользователя ввести следующие данные о путешествии:

    Место назначения.
    Дату начала путешествия.
    Длительность путешествия (в днях).

Затем программа использует этот объект для вывода информации о путешествии.

Sample Input 1:

Магадан
12.12.2023
неопределенное количество

Sample Output 1:

12.12.2023 вы отправляетесь в Магадан на неопределенное количество дней

Sample Input 2:

Гонконг
11.05.2025
7

Sample Output 2:

11.05.2025 вы отправляетесь в Гонконг на 7 дней

Sample Input 3:

Бразилиа
31.08.2024
12

Sample Output 3:

31.08.2024 вы отправляетесь в Бразилиа на 12 дней

*/

let dest = prompt();
let data = prompt();
let time = prompt();

let trip = {
    dest,
    data,
    time,
};

console.log(trip.data, 'вы отправляетесь в', trip.dest, 'на', trip.time, 'дней');
