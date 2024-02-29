/*

На вход подаётся число - год.

    Нужно вывести "YES", если год является високосным, иначе "NO".

 

    Високосный год - это год, который имеет одну дополнительную день, в феврале, 
    по сравнению с обычными годами. Этот дополнительный день добавляется к 28 дням февраля, делая его длиной 29 дней. 
    В обычных годах, февраль имеет 28 дней.

Чтобы год считался високосным, он должен соответствовать следующим правилам:

    Год делится на 4 без остатка. Например, 2024, 2028, 2032 и так далее.

    Если год также делится на 100 без остатка, он должен делиться на 400 без остатка, чтобы быть високосным. 
    Например, 2000 год был високосным, потому что он делится на 400 без остатка, но 1900 год не был високосным, 
    потому что он делится на 100 без остатка, но не делится на 400 без остатка.

Sample Input 1:

2000

Sample Output 1:

YES

Sample Input 2:

2048

Sample Output 2:

YES

Sample Input 3:

3000

Sample Output 3:

NO

*/

let year = Number(prompt());
if (year%400==0) {
    console.log("YES");} 
else if (year%4==0 && year%100 !=0) {
    console.log("YES");}
else {console.log("NO");}
