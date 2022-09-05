import re
"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.match("AB", s)
print(result)
"""


"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.search("CM", s)
print(result)
"""

"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.search("CM", s)
print(result[0])
"""


"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.findall("CM", s)
print(result)
"""

"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.split("/", s)
print(result)
"""

"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.split("/", s, maxsplit=3)
print(result)
"""

"""
s = "AB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CMAB/CM"
result = re.sub("A", "D", s)
print(result)
"""


s = "A"
result = re.fullmatch("A", s)
print(result)
