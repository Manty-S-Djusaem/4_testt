from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('ToDo')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

ws.mainloop()

frame = Frame(ws)
frame.pack(pady=10)

task_list = [
    'Create ToDo'
]

lb = Listbox(
    frame,
    width=10,
    height=5,
    fg='#464646',
    selectbackground='#a6a6a6',
    activestyle="none",
)
