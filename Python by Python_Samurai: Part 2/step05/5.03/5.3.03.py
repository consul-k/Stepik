lst = ['не забыть дышать', 'умыть себя', 'поесть чебурек',
       'убрать лоток', 'убрать лоток кота', 'микроуспокоить микроволновку']

# продолжите решение здесь
def func(todo_list, num=3):
    result = ""
    for i, item in enumerate(todo_list, num):
        result += f"{i}. {item}\n"
    return result
