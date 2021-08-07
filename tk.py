from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Registration Form')
root.geometry('300x150')


def click_button():
	root.destroy()

r_txt1 = Label(text='Complete registration please...').pack()
r_txt2 = Label(text='Enter login:').pack()
r_f1 = Entry().pack()
r_txt3 = Label(text='Enter password:').pack()
r_f2 = Entry(show = '*').pack()
btn = Button(bg='red', text='Finish!', width=10, height=1, command = click_button).pack()


root.resizable(width=False, height=False)

root.mainloop()