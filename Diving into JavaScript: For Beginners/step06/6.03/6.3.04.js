/*

Перед вами программа, которая сперва запрашивает у пользователя сумму, а потом спрашивает, какую операцию он хочет с ней совершить: 
внести эту сумму на счет или снять эту сумму со счета. Если сумма снятия превышает баланс, программа выводит сообщение о недостатке средств. 
Вставьте вместо троеточий верные инструкции.

Sample Input 1:

500
внести

Sample Output 1:

1000

Sample Input 2:

400
снять

Sample Output 2:

100

Sample Input 3:

600
снять

Sample Output 3:
Недостаточно средств на счете

*/

let bankAccount = {
  balance: 500,

  deposit: function(amount) {
    this.balance += amount;
  },

  withdraw: function(amount) {
    this.balance -= amount;
  },
};

const amount = Number(prompt());
const choice = prompt()
if (choice === "внести") {
    bankAccount.deposit(amount);
    console.log(bankAccount.balance);
} else if (choice === "снять") {
    if (amount > bankAccount.balance) {
        console.log('Недостаточно средств на счете');
    } else {
        bankAccount.withdraw(amount);
        console.log(bankAccount.balance);
    }
}
