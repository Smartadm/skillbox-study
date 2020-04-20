# -*- coding: utf-8 -*-

# Пространство имён (namespace) — это набор связей имён с объектами
# (а под капотом - словарь!)

# Примеры пространств имён:
# - локальные имена при вызове функции
# - глобальные имена в модуле
# - набор встроенных имён: функций вроде abs() print()


###
# пространство имен текущего модуля
# то что использовали с самого начала и не задумывались

x = 'GLOBO'


def func_1():
    x = 'LOCO'
    print('x in f1 =', x)


print('x =', x)

###
# пространство имен внешнего модуля

import module_1

# Доступ к именам происходит через точку после имени пространства имен - имени модуля
# Вообще, когда используется точка, то говорят о доступе к атрибутам обьекта
# У обьекта модуль есть аттрибуты - переменные из его пространства имен

print(module_1.x)
module_1.func_2()

###
# Мы можем добавлять или изменять значения переменных в пространстве имен модуля

module_1.abc = 'some string'

module_1.x = 'INJECTO'

print(module_1.x)
module_1.func_2()

# И даже удалять!
del x
del module_1.x
module_1.func_2()

# Такой подход называется манки патчингом (Monkey patch, см. https://goo.gl/yyxnH7)
# Мы у готового модуля что-то меняем внутри и надеемся что он будет работать
# Понятно, что изменения будут сохраняться только в рамках текущего запуска программы,
# в исходниках ничего не меняется


###
# Оператор global указывает что переменная берется из пространства имен текущего модуля

def func_3():
    global x
    x = 'LOCO'
    print('x in f1 =', x)


# print(x)
func_3()
print(x)

###
# globals() - встроенная функция, которая возвращает словарь глобальных имен


some_string = 'какая? да никакая! никакусенькая...'

print(globals())


###
# locals() - встроенная функция, которая возвращает словарь локального пространства имен

def func_4():
    x = 'LOCO'
    print(locals())


print(globals())

func_4()