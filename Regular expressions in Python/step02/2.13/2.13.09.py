'''

Найдите все слова, которые начинаются на n или N.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из букв латинского алфавита нижнего и верхнего регистров, -
    Начинается на n или N
    Не может быть подпоследовательностью

Sample Input 1:

n-word some spam Nail ещё какой-то текст nature Ninja Nice normal

Sample Output 1:

n-word Nail nature Ninja Nice normal

Sample Input 2:

_n-word 0n-word 1n-word 2n-word 3n-word 4n-word -n-word

Sample Output 2:

Sample Input 3:

n-w0rd n_w0rd

Sample Output 3:

'''

regex = r'\b(?<!\S)[Nn]\S[A-Za-z]{2,}\b'
