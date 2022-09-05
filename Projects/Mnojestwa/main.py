"""
numbers = {1,2,4,67}
print(numbers)
"""

"""
numbers = set()
print(type(numbers))
"""

"""
numbers = set([1,1,2,4,2])
print(numbers)
"""

"""
numbers = {1,2,2,4,5,6,7}
for i in numbers:
    print(i)
"""

"""
numbers = {1,2,3,4,5,6,7}
print(3 in numbers)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers.add(58)
print(numbers)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers.discard(58)
print(numbers)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers.remove(58)
print(numbers)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers.pop()
print(numbers)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers.union(numbers2)
print(numbers3)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers | numbers2
print(numbers3)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers.intersection(numbers2)
print(numbers3)
"""


"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers & numbers2
print(numbers3)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers - numbers2
print(numbers3)
"""


"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers2 - numbers
print(numbers3)
"""

"""
numbers = {1,2,3,4,5,6,7}
numbers2 = {2,8,3,64,55}
numbers3 = numbers2.copy()
print(numbers3)
"""

"""
numbers = {1,2,3,4,5,6,7}
print(len(numbers))
"""

"""
numbers = frozenset({1,2,3,4,5,6,7})
print(numbers)
"""

numbers = frozenset({1,2,3,4,5,6,7})
numbers.add(9)
print(numbers)
