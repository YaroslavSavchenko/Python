print("Введи 2 числа 'а' и 'b', чтоб в сумме было 10")
x = int(input("Введите а = "))
y = int(input("Введите b = "))
#if (type(x) or type(y) != int):
#    print("Непредвиденное условие, пробуйте снова!",type(x) )
def summa(a,b):
    if (a+b==10):
        print("Верно, спасибо!")
    elif(a<0 or b<0):
        print("Значение 'а' и 'b' должны быть положительными, попробуйте снова!")
    else:
        s = a + b
        print("Не верно, сумма равна", s, "а должна быть 10. Пробуй ещё раз!")


summa(x,y)
while x+y != 10:
    x = int(input("Введите а = "))
    y = int(input("Введите b = "))
    summa(x,y)
