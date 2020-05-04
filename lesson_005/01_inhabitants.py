# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

import room_1, room_2
print(*room_1.folks, 'live in room 1', sep=(', '))
print(*room_2.folks, 'live in room 2')