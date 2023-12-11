'''

Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. Ключами словаря на любом уровне могут быть только строки, значения - только числа. 

Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, соединенных знаком _

Для этого необходимо определить рекурсивную функцию flatten_dict. Она должна принимать вложенный словарь и возвращать плоский

Ниже приведены несколько способов решения вышеуказанной задачи.

nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}

flatten_dict(nested) => {'Germany_berlin': 7,
                         'Europe_italy_Rome': 3,
                         'USA_washington': 1,
                         'USA_New York': 4}

nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}

flatten_dict(nested) => {'Q_w_E_r_T_y': 123}

not_nested = {'a': 100, 'b': 200}

flatten_dict(not_nested) => {'a': 100, 'b': 200}

Ваша задача только написать определение функции flatten_dict

'''

def flatten_dict(d: dict) -> dict:
    res = {}
    for k, v in d.items():
        if isinstance(v, int):
            res.update({k:v})
        if isinstance(v, dict):
            for key, value in flatten_dict(v).items():
                res.update({k +'_' + key: value})
    return res
