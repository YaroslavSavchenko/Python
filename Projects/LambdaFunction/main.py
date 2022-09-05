"""
# Обычная функция
def rectangle_area(a,b):
    return a * b
print(rectangle_area(17,14))
"""

"""
# Те же действия через Лямбда-функцию
print((lambda a,b: a * b)(17,14))
"""

"""
# Свой вариант с Лямбда-функцией
func = (lambda a, b: a * b)(17,24)
print(func)
"""


# Другой пример
"""
def maximum(a,b):
   if a > b:
      return a
   else:
      return b
print(maximum(25,17))
"""
# Те же действия через Лямбда-функцию
# print((lambda a,b: a if a > b else b)(25,17))