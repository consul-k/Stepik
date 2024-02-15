/*

Перед вами программа, которая должна запрашивать баланс банковского счета у пользователя и выводить сообщение о балансе в заявленном формате. 
Вставьте вместо многоточия объявление метода для объекта.

Sample Input 1:

800

Sample Output 1:

Ваш текущий баланс: 800 долларов

Sample Input 2:

5

Sample Output 2:

Ваш текущий баланс: 5 долларов

*/

const balance = Number(prompt())        
let bankAccount = {
  balance,
  checkBalance() {
      console.log('Ваш текущий баланс:',this.balance,'долларов')
  }
};
bankAccount.checkBalance();
