'''

Вы получили доступ к секретному чату, в котором часто дарят ключи от Windows 7, и решили украсть один из них, т.к. у вас не активирован Windows 7. Вы выкачали все сообщения от новых к старым и проходите по ним программой. 
Что нужно сделать:

 Нужно найти первый попавшийся ключ. Нужные ключи в чате всегда отправляют в виде:

Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

    X - любая цифра или латинская буква в верхнем регистре
    Перед нужным ключом должна стоять строка Activation key:

Тестовые данные:
Входные данные:

На вход программе подаётся 5 строк. Гарантируется, что в этих строках есть как минимум 1 ключ.
Выходные данные:

Выведите в консоль ключ, который был найден. Только ключ. Другие данные не нужны.

Sample Input 1:

Hi
Here is my Activation key: PKRHK-6622Q-T49PV-CC3PX-TRX2Y
Bye
Test
Lmao

Sample Output 1:

PKRHK-6622Q-T49PV-CC3PX-TRX2Y

Sample Input 2:

Would you care for1 a cup of tea?
Only if you’re having one.
CM0T1-6W7ZJ-XY0Z3-ZROM3-BDLZ9
Yeah I have one and I have one Activation key: BR3DD-WJ2D6-RM84G-BHWQK-WFHW3
Do you take milk and sugar?

Sample Output 2:

BR3DD-WJ2D6-RM84G-BHWQK-WFHW3

Sample Input 3:

I expect you could do with
a cup of tea, couldn’t you?
Activation key: A70PM-KQ_BA-HYF2D-16CMK-OM4FP
Guys one Activation key: C7KYW-CBKVC-DPC82-7TPKD-Y8T2C for you
TY BRO!

Sample Output 3:

C7KYW-CBKVC-DPC82-7TPKD-Y8T2C

Sample Input 4:

Activation key: A70PM-KQ-BA-HYF2D-16CMK-OM4FP
JFP9D-7C4Z9-XHFMD-KH3TX-NTS6Z
Activatin key: ONHVS-A705Q-QIWMB-3TRKD-93JQV
gg key: J4DP3-WT02L-VK1DN-36ET7-MEKYI
Activation key: VMXSA-5FPC7-ERNTC-XG3YO-EG9W6 

Sample Output 4:

VMXSA-5FPC7-ERNTC-XG3YO-EG9W6 

Sample Input 5:

Activation key: ZxHMR-TVFQE-QUEP7-ZRYOV-7SPEX
JFP9D-7C4Z9-XHFMD-KH3TX-NTS6Z
Activatin key: ONHVS-A705Q-QIWMB-3TRKD-93JQV
gg key: J4DP3-WT02L-VK1DN-36ET7-MEKYI
Activation key: 9KAOG-UTB4I-6JAE3-75BR2-IB27P

Sample Output 5:

9KAOG-UTB4I-6JAE3-75BR2-IB27P

Sample Input 6:

Hi
Here is my Activation key: PKRHKF6622QGT49PVVCC3PX3TRX2Y
Bye
Activation key: 9KAOG-UTB4I-6JAE3-75BR2-IB27P
Lmao

Sample Output 6:

9KAOG-UTB4I-6JAE3-75BR2-IB27P

'''
