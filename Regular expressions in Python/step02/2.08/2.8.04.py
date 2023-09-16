'''

Напишите регулярное выражение, которое найдёт все IMEI в тексте.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из 15 арабских цифр
    Не является подпоследовательностью

Sample Input 1:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent imperdiet, justo id interdum congue, lectus enim maximus metus, non bibendum mauris magna egestas justo. Vivamus sapien tortor, 573458344082324 mollis at porttitor egestas, 348530789534050 molestie vitae lorem. Integer ante odio, egestas non magna id, rhoncus vehicula felis. Vivamus ultrices dictum tellus, vitae sodales enim mollis at. Curabitur bibendum, 784209482238423 nunc ac sagittis convallis, metus nisi lobortis odio, sed ultricies massa nisl ac massa. Etiam vel tellus vitae 375440983243456 sapien convallis imperdi 987547893450923 et quis in ex. Sed id suscipit turpis. Sed in lacinia quam. Sed hendrerit dui scelerisque, hendrerit ex sed, vehicula nisl. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 

Sample Output 1:

573458344082324 348530789534050 784209482238423 375440983243456 987547893450923

Sample Input 2:

5 64 370 0645 18792 366304 4542165 35805629 752639441 0857473968 75850129794 625761432970 3767484986023 28736415208410 8621053597912443 34021936729874856 746418350059863292 5839940613087674252

Sample Output 2:

'''

regex = r'\b\d{15}\b'
