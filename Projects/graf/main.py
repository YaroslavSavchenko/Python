
from tkinter import *
def click():
    number = int(text_input.get())
    message = ""
    for i in range(1,number+1,1):
        s = i * number
        mi = str(i)
        mr = str(number)
        ms = str(s)
        count = str(mi + " x " + mr + " = " + ms + "\n")
        message += count
        #textbox2["text"] = message
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2.insert(END, message)
    textbox2.insert(END, "\n")

def clear():
    textbox2.delete("1.0","end")
    textbox2["bg"] = "white"
    textbox2["fg"] = "black"

def save():
    get_text = textbox2.get("1.0","end")
    file = open("table.txt","w")
    file.write(get_text)
    file.close()

def open_file():
    load_file = open("table.txt", "r")
    textbox2.insert(END,load_file.read())
    load_file.close()

window = Tk()
window.geometry("550x500")
window.title("Таблица умножения")

label1 = Label(text = "Укажите номер для построения таблицы умножения: ")
label1.place(x = 30, y = 20)

text_input = Entry(text = "")
text_input.place(x = 350, y = 20, width = 30, height = 25)
text_input["justify"] = "center"
text_input.focus()

button1 = Button(text = "Построить", command = click)
button1.place(x = 400, y = 20, width = 120, height = 25)

textbox2 = Text()
textbox2.place(x = 35, y = 50, width = 300, height = 400)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

scroll = Scrollbar(textbox2)
scroll.pack(side = 'right', fill = 'y')
scroll['command'] = textbox2.yview
textbox2['yscrollcommand'] = scroll.set

button2 = Button(text = "Очистить", command = clear)
button2.place(x = 400, y = 60, width = 120, height = 25)

button3 = Button(text = "Сохранить", command = save)
button3.place(x = 400, y = 90,width = 120, height = 25)

button4 = Button(text = "Открыть файл", command = open_file)
button4.place(x = 400, y = 120,width = 120, height = 25)
window.mainloop()


