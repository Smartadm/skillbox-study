# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# TODO здесь ваш код

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
month_days_count = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month_days_name = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
month_days_id = list(month_days_count.keys())
if month in month_days_id:
    print('You choose ', month_days_name.get(month),', there is ', month_days_count.get(month), ' days in it.', sep='')
else:
    print('Wrong input, restart!')