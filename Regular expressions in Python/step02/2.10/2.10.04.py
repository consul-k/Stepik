'''

Напишите регулярное выражение, которое найдёт все повторяющиеся последовательности из двух цифр, которые идут друг за другом. Используйте нумерованные группы.
Что нужно найти:

Нужно найти последовательности из 2 одинаковых арабских цифр

Sample Input 1:

6996966969

Sample Output 1:

9696 6969

Sample Input 2:

534535345377777753453

Sample Output 2:

5353 7777

Sample Input 3:

0000010102020303040405050606070708080909101011111212131314141515161617171818191920202121222223232424252526262727282829293030313132323333343435353636373738383939404041414242434344444545464647474848494950505151525253535454555556565757585859596060616162626363646465656666676768686969707071717272737374747575767677777878797980808181828283838484858586868787888889899090919192929393949495959696979798989999

Sample Output 3:

0000 0101 0202 0303 0404 0505 0606 0707 0808 0909 1010 1111 1212 1313 1414 1515 1616 1717 1818 1919 2020 2121 2222 2323 2424 2525 2626 2727 2828 2929 3030 3131 3232 3333 3434 3535 3636 3737 3838 3939 4040 4141 4242 4343 4444 4545 4646 4747 4848 4949 5050 5151 5252 5353 5454 5555 5656 5757 5858 5959 6060 6161 6262 6363 6464 6565 6666 6767 6868 6969 7070 7171 7272 7373 7474 7575 7676 7777 7878 7979 8080 8181 8282 8383 8484 8585 8686 8787 8888 8989 9090 9191 9292 9393 9494 9595 9696 9797 9898 9999

'''

regex = r'([0-9]{2})\1'
