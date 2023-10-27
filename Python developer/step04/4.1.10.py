'''

Представим, что вы программируете hr-сервис по работе с вакансиями. Обычно в языках программирования есть множество различных фреймворков,
и каждый из них относится к определенному языку программирования и специальности. 
Напишите программу, которая по названию фреймворка будет определять язык и профессию человека.

    Flask, Django, Fast-API – Python(<framework>),Backend-dev
    Angular, React, Vue – JavaScript/TypeScript(<framework>),Frontend-dev
    Flutter, React Native – JavaScript(<framework>),Cross-Mobile-dev
    Pandas, skit-learn, keras – Python(<framework>),Data-Scientist

В случае если фреймворк еще не известен – выведете "модель еще не обучена"

Ввод:

s – строка с названием фреймворка

Вывод:

Через запятую – lang(framework), profession

Sample Input 1:

Fast-API

Sample Output 1:

Python(Fast-API),Backend-dev

Sample Input 2:

Tornado

Sample Output 2:

модель еще не обучена

Sample Input 3:

Python

Sample Output 3:

модель еще не обучена

Sample Input 4:

Django

Sample Output 4:

Python(Django),Backend-dev

Sample Input 5:

Flask

Sample Output 5:

Python(Flask),Backend-dev

Sample Input 6:

Angular

Sample Output 6:

JavaScript/TypeScript(Angular),Frontend-dev

Sample Input 7:

React

Sample Output 7:

JavaScript/TypeScript(React),Frontend-dev

Sample Input 8:

Vue

Sample Output 8:

JavaScript/TypeScript(Vue),Frontend-dev

Sample Input 9:

Flutter

Sample Output 9:

JavaScript(Flutter),Cross-Mobile-dev

Sample Input 10:

React Native

Sample Output 10:

JavaScript(React Native),Cross-Mobile-dev

Sample Input 11:

Pandas

Sample Output 11:

Python(Pandas),Data-Scientist

Sample Input 12:

skit-learn

Sample Output 12:

Python(skit-learn),Data-Scientist

Sample Input 13:

keras

Sample Output 13:

Python(keras),Data-Scientist

'''

match f:=input():
    case 'Flask' | 'Django' | 'Fast-API':
        print(f"Python({f}),Backend-dev")
    case 'Angular' | 'React' | 'Vue':
        print(f"JavaScript/TypeScript({f}),Frontend-dev")
    case 'Flutter' | 'React Native':
        print(f"JavaScript({f}),Cross-Mobile-dev")
    case 'Pandas' | 'skit-learn' | 'keras':
        print(f"Python({f}),Data-Scientist")    
    case _:
        print("модель еще не обучена")
