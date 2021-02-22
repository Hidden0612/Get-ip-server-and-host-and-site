
import os, socket
import tkinter as tk

def response(a):
    b = socket.gethostbyname(a)
    d = "\n\n\n Mr Hidden \n@Hidde0612\n\ngithub.com/Hidden0612"
    return b + d

def do(a):
    label['text'] = response(a)

root = tk.Tk()
root.title('Ip')

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

frame = tk.Frame(root, bg='yellow', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Modern', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get IP', bd=0, bg='white', fg='black', font=60, command=lambda:do(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='yellow', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Modern', 15), anchor='nw', bg='grey', fg='white', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()