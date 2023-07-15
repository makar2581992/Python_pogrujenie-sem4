# Напишите функцию принимающую на вход только ключевые параметры и возвращающую
# словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def dicts(**kwargs):
    list1 = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        list1[v] = k
    return list1


print(dicts(human='Ivan', lesson={'Biology': 2, 'Foreign language': 1}, car=['LADA', 'UAZ', 'Daewoo'],
                     sport={'boxing', 'jiu-jitsu', 'tennis'}))