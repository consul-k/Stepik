'''

Напишите регулярное выражение, которое найдёт все слова, содержащие в себе букву а.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Используются буквы кириллического алфавита нижнего и верхнего регистров
    Последовательность должна содержать как минимум одну букву а
    Заглавную А искать не нужно
    Последовательность не может быть подпоследовательностью

Sample Input 1:

Равным образом постоянный количественный рост и сфера нашей активности напрямую зависит от экономической целесообразности принимаемых решений! Не следует, однако, забывать о том, что консультация с профессионалами из IT играет важную роль в формировании системы масштабного изменения ряда параметров. Дорогие друзья, консультация с профессионалами из IT напрямую зависит от существующих финансовых...

Sample Output 1:

Равным образом сфера нашей активности напрямую зависит целесообразности принимаемых однако забывать консультация профессионалами играет важную формировании масштабного ряда параметров консультация профессионалами напрямую зависит финансовых

Sample Input 2:

В частности, разбавленное изрядной долей эмпатии, рациональное мышление создаёт предпосылки для системы массового участия. Как уже неоднократно упомянуто, предприниматели в сети интернет и по сей день остаются уделом либералов, которые жаждут быть объективно рассмотрены соответствующими инстанциями. Ясность нашей позиции очевидна: разбавленное изрядной долей эмпатии, рациональное мышление не даёт нам иного выбора, кроме определения поставленных обществом задач.

Sample Output 2:

частности разбавленное эмпатии рациональное создаёт массового участия Как неоднократно предприниматели остаются либералов жаждут рассмотрены инстанциями нашей очевидна разбавленное эмпатии рациональное даёт нам выбора поставленных задач

Sample Input 3:

0а0 1а1 2а2 3а3 4а4 5а5 6а6 7а7 8а8 9а9 _а_

Sample Output 3:

Sample Input 4:

Не творог, а творог!!! 🤬

Sample Output 4:

а

'''

regex = r'\b[Б-ЯЁа-я]*а[а-яё]*\b'
