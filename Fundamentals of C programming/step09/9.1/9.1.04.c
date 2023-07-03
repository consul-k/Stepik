/*

Определить тип символа.

Входные данные:
Один символ. Либо буква латинского алфавита, либо цифра.

Выходные данные:
digit -- если это цифра, en -- если это буква латинского алфавита. В иных случаях вывести error.

Sample Input 1:

g

Sample Output 1:

en

Sample Input 2:

5

Sample Output 2:

digit

*/

#include <stdio.h>

int main() {
  char c;
    c = getchar();
    int n = c;
    if(65 <= n && n <= 90)
        printf("en");
    else if(97<= n && n <= 122)
        printf("en");
    else if(48 <= n && n <= 57)
        printf("digit");
    else printf("error");
  return 0;
}
