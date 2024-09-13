from math import sin

def square(number):
    return number**2

def cube(number):
    return number**3

def radical(number):
    return number**(0.5)

def module(number):
    return abs(number)

def sinus(number):
    return sin(number)

commands = {'квадрат': square, 'куб': cube, 'корень': radical, 'модуль': module, 'синус': sinus}
n = int(input())
command = input()

print(commands[command](n))
