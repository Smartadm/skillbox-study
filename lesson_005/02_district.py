# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1 import room1 as dcsh1r1
from district.central_street.house1 import room2 as dcsh1r2
from district.central_street.house2 import room1 as dcsh2r1
from district.central_street.house2 import room2 as dcsh2r2
from district.soviet_street.house1 import room1 as dssh1r1
from district.soviet_street.house1 import room2 as dssh1r2
from district.soviet_street.house2 import room1 as dssh2r1
from district.soviet_street.house2 import room2 as dssh2r2

dist_folks = []
dist_folks.extend(dcsh1r1.folks)
dist_folks.extend(dcsh1r2.folks)
dist_folks.extend(dcsh2r1.folks)
dist_folks.extend(dcsh2r2.folks)
dist_folks.extend(dssh1r1.folks)
dist_folks.extend(dssh1r2.folks)
dist_folks.extend(dssh2r1.folks)
dist_folks.extend(dssh2r2.folks)

all_folks = ', '.join(dist_folks)
print('In my district live', all_folks)


