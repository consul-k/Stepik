/*

Для целого числа KK (от 1 до 99 включительно) напечатать фразу «Мне K лет», учитывая при этом, что при некоторых значениях KK слово «лет» надо заменить на слово «год» или «года». Например, 11 лет, 22 года, 51 год.

Входные данные: Одно целое число KK, 1≤k≤991≤k≤99

Выходные данные: Фраза с правильным окончанием

Sample Input:

11

Sample Output:

Мне 11 лет

*/

#include <stdio.h>
#include <locale.h>
int main() {
    setlocale(LC_ALL, "");
 int k;
    scanf("%d", &k);
    switch (k){
        case 11:
        case 12:
        case 13:
        case 14: printf("Мне %d лет\n", k);break;
        default  : 
			switch (k % 10){
        		case 1: printf("Мне %d год\n", k);break;
        		case 2:
        		case 3:
        		case 4: printf("Мне %d года\n", k);break;
        		case 5:
        		case 6:
        		case 7:
        		case 8:
        		case 9:
        		case 0:printf("Мне %d лет\n", k);break;
        		default  : break;    
    		}
	    
    }
            
     
  return 0;
}
