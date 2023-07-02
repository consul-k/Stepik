/*

Определить правильность даты, введенной с клавиатуры (число — от 1 до 31, месяц — от 1 до 12). Если введены некорректные данные, то сообщить об этом.

Входные данные:
Два целых числа: первое -- число в месяце, второе -- номер месяца в году.

Выходные данные:
Строка correct, если дата правильная, и строка error, если подобной даты не может быть.

Уточнение:
Предполагаем, что в феврале 29 дней.

Sample Input:

19 5

Sample Output:

correct

*/

#include <stdio.h>

int main() {
  int day, month;
  scanf("%d %d", &day, &month);
  int limit;
  switch (month){
      case 1:
      case 3:
      case 5:
      case 7:
      case 8:
      case 10:
      case 12 : limit = 31; break;
      case 2: limit = 28; break;
      default: limit = 30; break;
  }
  if (day > limit || day < 1 || month > 12 || month < 1)
      printf("error");
  else
      printf("correct");
  return 0;
}
