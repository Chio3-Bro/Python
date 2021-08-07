#Счётчик кликов для майнкрафт-юзеров

from tkinter import *

#Кол-во кликов
clicks = 0
 
#Фун-ия по клику
def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
 
#Параметры переменной
root = Tk()
root.title("WinHelpClicks")
root.geometry("220x50")
 
#Сама кнопка
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button).pack()

 
root.mainloop()
