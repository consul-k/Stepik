'''

Допишите код, чтобы получить нужный результат.

Sample Input:

Sample Output:

Hello!Hello!Hello!

'''

class Hello:
    def __init__(self, say):
        self.say = say

    # Ваш код
    def __mul__(self, other):
        return self.say * other

lang = Hello('Hello!')
print(lang * 3)  # Hello!Hello!Hello!
