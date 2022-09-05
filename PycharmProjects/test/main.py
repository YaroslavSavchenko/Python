
"""
def pars(n):
    c=""
    for i in n:
        if (i == "l"):
            continue
        c=c+i
    print(c)


name = "Hello world!!!"
pars(name)
"""


"""
mass = ["1",2,"text",4,"пять"]

for i in mass:
    if (i == "пять"):
        continue
    elif (i == "text"):
        continue
    print(i)
"""


"""
mass = ["1",2,"text",4,"пять"]
print(mass[-1])
"""

"""
mass = ["1",2,"text",4,"пять"]
mass.append(6)
print(mass)

sass=mass
sass.pop()
print(sass)

inn = mass.index(4)
print(inn)

length = mass
print(len(length))

zam = mass
zam[3] = "Zamena"
print(zam)
"""


"""
mass = [1,2,8,4,0,6,5,9]
mass.sort()
print (mass)

rev = mass
rev.sort(reverse = True)
print (rev)
"""

# -----------------Списки, Кортежи, Словари--------------
"""
kort = ("test",)

if (type(kort) == tuple):
    print('Получилось')
else:
    print("не получилось")
"""


"""
mass = ["errorrrr",1,2,3,4,5,6,7,"a","b","C"]
kort = (1,5,8,64,867,3456,"a","t","1344")

k = tuple(mass)
m = list(kort)
print(m)
print(k)
"""

"""
obj = {"Рука":2,"Нога":2,"Голова":1, "Пальцы":20, "Звук":"Голос", "Отдых":"Сон"}
#print(obj["Голова"])

del obj["Нога"]
print(obj)
"""



#print("Если нужно вывести текст:\n\t1.Пишем оператор \"print\"\n\t2.Указываем текст в кавычках\n\t3.Запускаем код\r* Примечание: можно использовать одинарные кавычки для print и наоборот:")

"""
a = "Полученный"
b = "Результат"
#print(a+" "+b)
#print(b[8])
c=0
d=0
n=0
for i in range(0,9,1):
    c = c+1
    #print(b[i])

while (n<c):
    n=n+1
    print(b[d])
    d=d+1

c(b)
print(b)
"""

#-------модули------------------
"""
import math
f = math.factorial(10)
print(f)

import math as f
print(f.factorial(10))

from math import factorial
print(factorial(10))
"""

#----------Файлы----------
"""
file = open("test1.txt", "w")
file.write("Запись данных")
file.close()

file = open("test1.txt", "r")
print(file.read())
file.close()

with open("test1.txt", "a") as file:
    file.write(" и добавление данных")

file2 = open("test2.xlsx", "w")
file2.write("Запись данных")
file2.close()
"""

#------------Обработка ошибок----------
"""
try:
    a = int(input("Введите А: "))
    b = int(input("Введите В: "))
    c = a / b
    res = str(c)
    print(c)
    with open("test3.txt","a") as file3:
        file3.write(res+", ")
except ZeroDivisionError:
    print("На 0 делить нельзя")
"""

"""
#-------------------Классы------------------
class Human():
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def result(self):
        return "Вы человек по имени "+self.name+ ", "+"который имеет "+self.gender+" пол"

n = input("Введите имя: ")
g = input("Введите пол: ")

person = Human(n,g)
res = person.result()
print(res)
with open("persons.txt","a") as person_file:
    person_file.write(res+". ")
"""

#-------------------Множества------------------
"""
numb = {1,2,7,9,56,68,84,35,2}
print(numb)
#numb2 = set()
#print(type(numb2))
m = []
for i in numb:
    print(i)
    m.append(i)
m.sort()
print("m = "+str(m))

print (2 in numb)

m2 = {1,2,3}
#print(m2)
if 3 in m2:
    m2.add(4)
if 2 in m2:
    m2.discard(2)
print(m2)

m3 = numb.union(m2)
print(m3)
m4 = numb | m2
print(m3)

m4 = numb.intersection(m2)
print(m4)
m5 = numb & m2
print(m5)

m6 = m2 - numb
print(m6)

m7 = numb.copy()
print(m7,"=",len(m7),"элементов")
"""
#-------------------Lambda-функции------------------
"""
print((lambda a,b:a*b)(10,12))
func = (lambda a,b:a if a > b else b)(10,22)
print(func)
"""

#-------------------Разное------------------
"""
#inp = input("Введите текст: ")
#print("Ваш текст имеет",len(inp),"символов")

a = 9
b = 5
c = a//b
d = a/b
e = a%b

print("c = ",c,"\nd = ",d, "\ne = ",e)
"""
#---------------Таблица умножения------------------
"""num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
 answer = i * num
 print(i, "x", num, "=", answer)
 """


"""
summ = 0
for i in range(0,5):
   namb = int(input("enter numb: "))
   answer = input("include number? (y/n)")
   if answer == "y":
       summ = summ + namb
print(summ)
"""

"""
numb = int(input("Введите число, чтоб угадать: "))
res = 20
count = 1
while numb != res:
   if numb < res:
       print("Ваше введенное число меньше")
   else:
       print("Ваше введенное число больше")
   count+=1
   numb = int(input("Повторите ввод, чтоб угадать: "))
print("Вы угадали! Ваше количество попыток: ", count,)
"""

"""
#-----------------Генератор чисел-----------------
import random
num = random.random()
num = num * 100
r = num // 1
print(int(r))

num2 = random.randint(0,9)
print("num2:",num2)

num3 = random.randint(0,1000)
num4 = random.randint(0,1000)
res = num3 / num4
print("randon (num3 / num4) =",res)

num5 = random.randrange(0,100,5)
print("num5 =",num5)

num6 = random.choice(["red","blue","green","black","brown","yellow"])
print("random color =",num6)

#--------------угадай число------------------------------
rand = random.randint(0,10)
numb = int(input("Введи число и угадай рандомный вариант: "))
total = 1
while numb != rand:
    rand = random.randint(0, 10)
    numb = int(input("Не угадал, попробуй ещё: "))
    total += 1
print("Поздравляю, ты угадал с",total,"раза")
"""

"""
file = open("Names.txt","a")
new = input("Введите имя: ")
file.write(new + "\n")
file.close()

file2 = open("Names.txt", "r")
print(file2.read())
"""
#---------------Просмотр состава имён(методов) модуля--------
"""
import math
#print(dir(math))
for i in dir(math):
    print(i)
"""

