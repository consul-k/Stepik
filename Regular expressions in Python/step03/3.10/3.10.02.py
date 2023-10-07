'''

Замените все цифры на X. Выведите полученную строку и количество совершённых замен.
Что нужно сделать:

Заменить все цифры в тексте на X.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Кортеж с изменённой строка и количеством совершённых замен.

Sample Input 1:

65,905 views  Nov 19, 2022 

Sample Output 1:

('XX,XXX views  Nov XX, XXXX ', 11)

Sample Input 2:

I am currently crying so hard right now. This is seriously the most beautiful, well put together story ever. I can’t believe how magical it was 1:12. That part truly made me shed a tear. And especially at 6:34 that part was just so truly heart touching words can not describe the series of emotions I felt. I absolutely loved the climax it had insanely excellent detail. Oh and we can’t forget the conclusion. The conclusion was the greatest and saddest conclusion I have ever seen better than any of the books I have read. Thank you so much for creating this absolute masterpiece. This is essentially the most important masterpiece of film history. It is a tragedy that this, it can’t be called a film, but a transcendent emotional experience, will be inaccessible for most. It beautifully encapsulates the human struggle to its basics; suffering, pleasure, faith, despair. It connects with the characters within the viewers, individuals suppressed within our own subconscious. It stays vibrant, fresh, and revolutionizes the art of storytelling and fs masterpiece. Especially when the chip spins, showing its lightly salt covered yellow skin. I can hear the crunch just from here, and so as the beautiful sound of the chip scraping the dark, smooth velvet floor.  The flavor, music and everything can be heard, tasted, seen and felt from a screen. You can really hear the breaths between the music artist, empathizing her love for this rotating chip. Truly what I call modern art. This was the most legendary performance by any piece of chip I have ever watched. The acting was top tier and very life changing. This is one of the greatest work from a piece of chip I have ever seen especially on 57:42.

Sample Output 2:

('I am currently crying so hard right now. This is seriously the most beautiful, well put together story ever. I can’t believe how magical it was X:XX. That part truly made me shed a tear. And especially at X:XX that part was just so truly heart touching words can not describe the series of emotions I felt. I absolutely loved the climax it had insanely excellent detail. Oh and we can’t forget the conclusion. The conclusion was the greatest and saddest conclusion I have ever seen better than any of the books I have read. Thank you so much for creating this absolute masterpiece. This is essentially the most important masterpiece of film history. It is a tragedy that this, it can’t be called a film, but a transcendent emotional experience, will be inaccessible for most. It beautifully encapsulates the human struggle to its basics; suffering, pleasure, faith, despair. It connects with the characters within the viewers, individuals suppressed within our own subconscious. It stays vibrant, fresh, and revolutionizes the art of storytelling and fs masterpiece. Especially when the chip spins, showing its lightly salt covered yellow skin. I can hear the crunch just from here, and so as the beautiful sound of the chip scraping the dark, smooth velvet floor.  The flavor, music and everything can be heard, tasted, seen and felt from a screen. You can really hear the breaths between the music artist, empathizing her love for this rotating chip. Truly what I call modern art. This was the most legendary performance by any piece of chip I have ever watched. The acting was top tier and very life changing. This is one of the greatest work from a piece of chip I have ever seen especially on XX:XX.', 10)

Sample Input 3:

XYZ

Sample Output 3:

('XYZ', 0)

Sample Input 4:

X111X

Sample Output 4:

('XXXXX', 3)

'''

import re

result = re.subn(r'[0-9]', 'X', input())
print(result)
