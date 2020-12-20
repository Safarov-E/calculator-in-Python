from tkinter import *

root = Tk()
root.title("Калькулятор")
root.resizable(False, False)

buttons = (('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'))

result = Label(root, text="0", font="Tahoma 20", bd=10)
result.grid(row=0, column=0, columnspan=4)

for row in range(4):
    for column in range(4):
        button = Button(root, text=buttons[row][column], font="Tahoma 20")
        button.grid(row=row+1, column=column, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")

w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)

root.geometry("+{0}+{1}".format(x, y))
root.mainloop()