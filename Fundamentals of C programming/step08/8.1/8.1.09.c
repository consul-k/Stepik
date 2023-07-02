/*

В заданном массиве поменять местами наибольший и наименьший элементы.

Входные данные:
Первая строка число N,(N>0)N,(N>0) -- длина массива. Длина массива не более 100 элементов. Вторая строка NN  натуральных чисел, записанных через пробел.

Выходные данные:
Новый массив, в котором на месте минимума(ов) стоит максимум, а на месте максимума(ов) стоит минимум. Остальные элементы массива остаются на прежних местах.

Sample Input:

5
10 93 22 75 12

Sample Output:

93 10 22 75 12

*/

#include <stdio.h>

int main() {
    const int quantity;
    scanf("%d", &quantity);  

    int arr[quantity];

    for(int i = 0; i < quantity; i++) {
        scanf("%d", &arr[i]);        
    }

    int max, min, i_min, i_max;
    i_min = 0;
    i_max = 0;
    min = max = arr[0];

    for(int i = 0; i < quantity; i++) {
        if(min > arr[i]) {
            min = arr[i];
            i_min = i;
        } else if(max < arr[i]) {
            max = arr[i];
            i_max = i;
        }
    }    

    for(int i = 0; i < quantity; i++) {
        if(i == i_min) {
            printf("%d ", arr[i_max]);
        } else if(i == i_max) {
            printf("%d ", arr[i_min]);
        } else {
            printf("%d ", arr[i]);
        }
    }
	return 0;
}
