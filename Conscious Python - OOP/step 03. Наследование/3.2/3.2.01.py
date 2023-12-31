'''

    Создайте два класса Minecraft и Roblox. Класс Roblox - будет дочерним классом Minecraft.
    В классе Minecraft создайте метод hello_creeper, который будет выводить на экран фразу - "Hello, Creeper!".
    В классе Roblox создайте метод hello_all, который будет вызывать метод hello_сreeper. Метод hello_all также будет выводить на экран фразу "Hello, Pozzy!" с помощью print.
    Создайте экземпляр hello класса Roblox.
    Вызовите метод hello_all, через экземпляр hello. Функцию print не нужно использовать.

В итоге, программа будет выводить на экран две фразы, как указано в примере ниже. 

Sample Input:

Sample Output:

Hello, Creeper!
Hello, Pozzy!


'''

class Minecraft:
    def hello_creeper(self):
        print('Hello, Creeper!')

class Roblox(Minecraft):
    def hello_all(self):
        super().hello_creeper()
        print('Hello, Pozzy!')
hello = Roblox()
hello.hello_all()
