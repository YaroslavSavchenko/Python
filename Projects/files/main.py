'''
# Запись в файл
file = open("test.txt","w")
file.write("Записано в файл!")
file.close()
'''

'''
# чтение файла
file = open("test.txt","r")
print(file.read())
file.close()
'''
'''
# Добавление файла
with open("test.txt","a") as file:
    file.write("Добавленный текст")
'''

'''
with open("test.txt","r") as file:
    print (file.read())
'''

# Обработка исключений

try:
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    print(a/b)
except ZeroDivisionError:
    print("На 0 делить нельзя!")

'''
# Тест с повторным запуском на ввод после ошибки
def inp():
    try:
        a = int(input("Введите а: "))
        b = int(input("Введите b: "))
        print(a/b)
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
        inp()
print(inp())
'''