from tkinter import *
 
clicks = 0
 
 
def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
 
root = Tk()
root.title("WinHelpClicks")
root.geometry("220x50")
 
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button).pack()

 
root.mainloop()