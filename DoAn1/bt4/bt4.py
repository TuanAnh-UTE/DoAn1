
from tkinter import *
from tkinter import messagebox

def Giai():
    sa = (txtA.get()).strip()
    sb = (txtB.get()).strip()
    if (sa == '') or (sb == ''):
        messagebox.showinfo('Warning','Ban phai nhap a va b')
        return
    try:
        a = float(sa)
    except ValueError:
        messagebox.showinfo('Warning','Ban phai nhap a b la con so')
        return

    try:
        b = float(sb)
    except ValueError:
        messagebox.showinfo('Warning','Ban phai nhap a b la con so')
        return
    
    if a == 0:
        if b == 0:
            result = 'PT VSN'
        else:
            result = 'PT VN'
    else:
        x = -b/a
        result = 'x = %.2f'%x
    lblKQ.set(result)

def Xoa():
    txtA.set('')
    txtB.set('')
    lblKQ.set('')
    entry_txtA.focus_set()

def quit():
    root.destroy()

root = Tk()

root.title("Bai01")
root.geometry('350x250')

txtA = StringVar()
txtB = StringVar()
lblKQ = StringVar()

Label(root, text="Giai Phuong Trinh Bac Nhat", font=("Arial", 15)).grid(column=0, row=0, columnspan=4)

Label(root, text="Nhap a ").grid(column=0, row=1)
entry_txtA = Entry(root, textvariable = txtA, width=18, justify='right')
entry_txtA.grid(column=1, row=1)
entry_txtA.focus_set()
Button(root, text="Giai", width=10, height = 1, command=Giai).grid(column=2, row=1)

Label(root, text="Nhap b ").grid(column=0, row=2)
Entry(root, textvariable = txtB, width=18, justify='right').grid(column=1, row=2)
Button(root, text="Xoa",  width=10, height = 1, command=Xoa).grid(column=2, row=2)

Label(root, text="Nghiem ").grid(column=0, row=3)
Label(root, textvariable = lblKQ, width = 15, height=1, borderwidth=2, relief='sunken', anchor='e').grid(column=1, row=3)

Button(root, text="Close", width=10, height = 1, command=quit).grid(column=0, row=4, columnspan=4)

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
