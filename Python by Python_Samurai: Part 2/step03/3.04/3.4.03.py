files = ['main.py', 'spisok.txt', '123.Py', 'paint.exe', 'tupik2003.mkv', 'foto.rar',
         'tanecjivota.Mkv', 'RDR2.eXe', 'blacklist.Txt', 'lesson.py', 'foto2.rAr',                            'hack_pintagon.pY', 'lesson.py'  
         ]        

# продолжите решение здесь
result = frozenset(word.lower() for word in files if word[-2:].lower() == 'py')
print(*sorted(result))
