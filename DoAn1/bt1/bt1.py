
from tkinter import *
from tkinter import ttk

win_width = 600
win_heigh = 400
geometry = "%dx%d" % (win_width,win_heigh)

red = 0
blue = 0
green = 0

points = [0, win_heigh, win_width/4*3/2, 0, win_heigh, win_heigh]

def setColor(scale, color):
    global red, blue, green
    if color == 0:
        red = scale.get()
    elif color == 1:
        green = scale.get()
    elif color == 2:
        blue = scale.get()
    updateColor()

def updateColor():
    global colorval
    colorval = "#%02x%02x%02x" % (red, green, blue)
    canvas.itemconfigure('shape', fill=colorval)

def changeShape():
    global colorval
    temp = Shapevar.get()
    canvas.delete('shape')
    if temp == 1:
        circle = canvas.create_oval(0, 0, win_heigh, win_heigh,fill=colorval, tag = 'shape')            # create_oval Tạo một hình tròn hoặc hình elip tại tọa độ đã cho. Phải mất hai cặp tọa độ; góc trên bên trái và dưới cùng bên phải của hình chữ nhật giới hạn cho hình bầu dục
    elif temp == 2:
        rect = canvas.create_rectangle(0, 0, win_width/4*3, win_heigh, fill=colorval, tag = 'shape')    # create_rectangle hai cặp tọa độ; góc trên bên trái và dưới cùng bên phải của hình chữ nhật
    elif temp == 3:
        triangle = canvas.create_polygon(points, fill=colorval, tag = 'shape')                          # create_polygon Tạo một mục đa giác phải có ít nhất ba đỉnh.




root = Tk()
root.title("BT1")
root.geometry(geometry)
root.resizable(False, False)

root.rowconfigure(0, weight=1)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)

shape = ttk.Frame(root, borderwidth=5)
shape.grid(column=1, row=0)
color = ttk.Frame(root, borderwidth=5)
color.grid(column=1, row=1)

canvas = Canvas(root, width=win_width/4*3, height=win_heigh)
triangle = canvas.create_polygon(points, fill="red", tag = 'shape')
canvas.grid(column=0, row=0,rowspan = 2, sticky=(N, W, E, S))

Shapevar = IntVar()
Text1 = Label(shape, text="Choose shape", font=("Arial", 15))
#Text1.pack( anchor = W )

Shape1 = Radiobutton(shape, text="Circle", variable=Shapevar, value=1, font=("Arial", 15), command=changeShape)
#Shape1.pack( anchor = W )

Shape2 = Radiobutton(shape, text="Rectangle", variable=Shapevar, value=2, font=("Arial", 15), command=changeShape)
#Shape2.pack( anchor = W )

Shape3 = Radiobutton(shape, text="triangle", variable=Shapevar, value=3, font=("Arial", 15), command=changeShape)
#Shape3.pack( anchor = W)
Shape3.select()

Text1.grid(column=0, row=0)
Shape1.grid(column=0, row=1, sticky=(W))
Shape2.grid(column=0, row=2, sticky=(W))
Shape3.grid(column=0, row=3, sticky=(W))

Colorvar = IntVar()
Text2 = Label(color, text="Choose color", font=("Arial", 15))
Redtext = Label(color, text="Red", font=("Arial", 15))
Redscale = Scale(color, from_=0, to=255, orient=HORIZONTAL, tickinterval=256, command=lambda x: setColor(Redscale, 0), cursor='hand2')
Redscale.set(255)
Greentext = Label(color, text="Green", font=("Arial", 15))
Greenscale = Scale(color, from_=0, to=255, orient=HORIZONTAL, tickinterval=256, command=lambda x: setColor(Greenscale, 1), cursor='hand2')
Bluetext = Label(color, text="Blue", font=("Arial", 15))
Bluescale = Scale(color, from_=0, to=255, orient=HORIZONTAL, tickinterval=256, command=lambda x: setColor(Bluescale, 2), cursor='hand2')

Text2.grid(column=0, row=0, columnspan=2)
Redtext.grid(column=0, row=1, sticky=(W))
Redscale.grid(column=1, row=1, sticky=(W))
Greentext.grid(column=0, row=2, sticky=(W))
Greenscale.grid(column=1, row=2, sticky=(W))
Bluetext.grid(column=0, row=3, sticky=(W))
Bluescale.grid(column=1, row=3, sticky=(W))

root.mainloop()