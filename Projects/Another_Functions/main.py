"""
def summa(*numbers):
    print(sum(numbers))
summa(7,8,9,1,10)
"""


"""
def brand(**kwargs):
    print(kwargs)
brand(a="Apple", b="Samsung")
"""

def brand(**kwargs):
    for x,y in kwargs.items():
        print(x, ":", y)
brand(a="Apple", b="Samsung")