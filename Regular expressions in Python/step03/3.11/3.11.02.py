'''

Передайте в метод ссылку, которая подаётся на вход программе.

Sample Input 1:

https://stepik.org/lesson/694442/step/3?unit=694231

Sample Output 1:

https://stepik\.org/lesson/694442/step/3\?unit=694231

Sample Input 2:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

Sample Output 2:

https://www\.youtube\.com/watch\?v=dQw4w9WgXcQ

Sample Input 3:

https://regex101.com/

Sample Output 3:

https://regex101\.com/

'''

import re

print(re.escape(input()))
