from tkinter import *

x = 5
y = 5
w = 100
h = 100
offset = 3

win_width = w*x + offset*2
win_heigh = h*y + offset*2
geometry = "%dx%d" % (win_width,win_heigh)

def cross(event):
    posx = (int) ((event.x - offset) / w)                                                                                                               #event.x va event.y la toa do cua vi tri bam chuot
    posy = (int) ((event.y - offset)/ h)
    if (flag[posy][posx]):
        canvas.delete("line%dx%d"%(posy, posx))                                                                                                         #xoa line
    else:                                                                                                                                               #them line
        id = canvas.create_line(posx*w+offset, posy*h+offset, (posx+1)*w+offset,
                               (posy+1)*h+offset, tag="line%dx%d"%(posy, posx),
                              width=offset)
        id = canvas.create_line((posx+1)*w+offset, posy*h+offset, posx*w+offset,
                               (posy+1)*h+offset, tag="line%dx%d"%(posy, posx),
                              width=offset)
    flag[posy][posx] = not flag[posy][posx]

root = Tk()
root.title("BT5")
root.geometry(geometry)
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.bind("<Button-1>", cross)  # lay event bam chuot trai

canvas = Canvas(root, width=win_width, height=win_heigh)
canvas.grid(column=0, row=0)

flag = []       # mang 2 chieu chua bolean, true la tick, false la chua tick

for i in range(y):
    temp = []
    for j in range(x):
        temp.append(False)      #them gia tri vao mang
        id = canvas.create_rectangle(j*w+offset, i*h+offset, (j+1)*w+offset, (i+1)*h+offset, width=offset, fill="white") #ve hinh vuong
    flag.append(temp)   #them gia tri vao mang

root.mainloop()
