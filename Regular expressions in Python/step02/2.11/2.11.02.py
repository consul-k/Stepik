'''

Напишите регулярное выражение, которое найдёт все символы /, слева и справа от которых ничего нет или стоят другие символы, не равные /.

Что нужно найти:
Нужно найти последовательности, подходящие по следующим условиям:

    Слева от неё не стоит /
    Справа от неё не стоит /
    Последовательность состоит из одного слеша: /

Sample Input 1:

k}e09lQS>:)*N\/OYp+N//;Oy6///hS/.T//O/n/(_oR///////eD?/nxeZOg2=j-Zw+-z}>5Sl[VX:}zaB:sL7fe</3>tgqk(8vP701}bcWnT~a/MR0	

Sample Output 1:

/ / / / / / /

Sample Input 2:

/text/

Sample Output 2:

/ /

Sample Input 3:

</=/>/?/@/A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P/Q/R/S/T/U/V/W/X/Y/Z/[/]/^/_/`/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/{/|/}/~/а/б/в/г/д/е/ё/ж/з/и/й/к/л/м/н/о/п/р/с/т/у/ф/х/ц/ч/ш/щ/ъ/ы/ь/э/ю/я/А/Б/В/Г/Д/Е/Ё/Ж/З/И/Й/К/Л/М/Н/О/П/Р/С/Т/У/Ф/Х/Ц/Ч/Ш/Щ/Ъ/Ы/Ь/Э/Ю/Я/ /!/"/#/$/%/&/\/'/(/)/*/+/,/-/.///0/1/2/3/4/5/6/7/8/9/:/;/

Sample Output 3:

/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

Sample Input 4:

oCx~;:ll]c+f2lPuF~8=rfU"8k}dPkKc]"nhA40D!.>#q6Z:.RhF%a7+R]rxv*YGyk[_g]0N<3\G830>PfM\FN#nQW<b[.3Kp\Y

Sample Output 4: 

'''

regex = r'(?<!/)/(?!/)'
