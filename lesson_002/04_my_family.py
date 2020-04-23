#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['me', 'son', 'wife']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['me', 185],
    ['wife', 180],
    ['son', 70]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('father`s height is', my_family_height[0][1], 'sm.')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

height_sum = 0
for i in my_family_height:
    height_sum += i[1]
print("Our summary height is", height_sum, "sm.")