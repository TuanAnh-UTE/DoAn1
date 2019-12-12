
from tkinter import *
from tkinter import ttk
import threading
from datetime import datetime

win_width = 800
win_heigh = 200
geometry = "%dx%d" % (win_width,win_heigh)

gap = 3
numgap = 20
w = 20
h = 50
h1 = 10
circle = w
stop = False
segments = [[w/2, 0, 0, h1, 0, h1+h, w/2, h1*2+h, w, h1+h, w, h1],
            [0, w/2, h1, 0, h1+h, 0, h1*2+h, w/2, h1+h, w, h1, w]]

colon = [[0, (h+h1*2)*2+gap*4+w - circle, circle, (h+h1*2)*2+gap*4+w ],
         [0, h+h1*2+gap*2+w/2, circle, h+h1*2+gap*2+w/2+circle]]

fSevenSegment = [   [1, 1, 1, 1, 1, 1, 0],     # 0
                    [0, 1, 1, 0, 0, 0, 0],     # 1
                    [1, 1, 0, 1, 1, 0, 1],     # 2
                    [1, 1, 1, 1, 0, 0, 1],     # 3
                    [0, 1, 1, 0, 0, 1, 1],     # 4
                    [1, 0, 1, 1, 0, 1, 1],     # 5
                    [1, 0, 1, 1, 1, 1, 1],     # 6
                    [1, 1, 1, 0, 0, 0, 0],     # 7
                    [1, 1, 1, 1, 1, 1, 1],     # 8
                    [1, 1, 1, 1, 0, 1, 1] ]    # 9

offset = [[1, 0, 0, 1, 0, 0, 1],  # nam ngang hay doc
          [w/2+gap, w+h+gap*2, w+h+gap*2, w/2+gap, 0, 0, w/2+gap], #offset x
          [0, w/2+gap, w/2+h+h1*2+gap*3, h*2+h1*4+gap*4, w/2+h+h1*2+gap*3, w/2+gap, w/2+h+h1*2-gap] ]  #offset y
tags = ["hour1", "hour2", "minute1", "minute2", "second1", "second2"] # tag cho tung shape

def createOffset(x, y):
    return [x, y, x, y, x, y, x, y, x, y, x, y]

#vẽ số 0-9, từ trái qua phải
def printDigit(digit, number):
    position = number*(h+w+h1*2+gap*2+numgap) + ((int)(number/2)*(circle+numgap))
    for i in range(7):
        if (fSevenSegment[digit][i]):
            temp = [sum(x) for x in zip(segments[offset[0][i]], createOffset(position+offset[1][i], offset[2][i]))]
            test = canvas.create_polygon(temp, fill="red", tag = tags[number])
            canvas.pack(side = RIGHT, fill = BOTH, expand = True)

root = Tk()
root.title("BT2")
root.geometry(geometry)

canvas = Canvas(root)
# draw colon
position = 4*(h+w+h1*2+gap*2+numgap) + (circle+numgap)
temp = [sum(x) for x in zip(colon[0], [position,0,position,0])]
canvas.create_oval(temp, fill="red")
temp = [sum(x) for x in zip(colon[1], [position,0,position,0])]
canvas.create_oval(temp, fill="red")

position = 2*(h+w+h1*2+gap*2+numgap)
temp = [sum(x) for x in zip(colon[0], [position,0,position,0])]
canvas.create_oval(temp, fill="red")
temp = [sum(x) for x in zip(colon[1], [position,0,position,0])]
canvas.create_oval(temp, fill="red")

#init value
now = datetime.now().time()
hour = now.hour
minute = now.minute
second = now.second
printDigit((int)(hour/10), 0)
printDigit((int)(hour%10), 1)
printDigit((int)(minute/10), 2)
printDigit((int)(minute%10), 3)
printDigit((int)(second/10), 4)
printDigit((int)(second%10), 5)

def update():
    global hour, minute, second, stop
    if stop:
        return
    threading.Timer(1, update).start()
    second += 1 
    if second >= 60:
        second = 0
        minute += 1
        if minute >= 60:
            minute = 0
            hour += 1
            if hour >= 24:
                hour = 0
            updateHour(hour)
        updateMinute(minute)
    updateSecond(second)
            
def updateSecond(value):
    canvas.delete(tags[5])
    printDigit(value%10, 5)
    if value%10 == 0:
        canvas.delete(tags[4])
        printDigit((int)(value/10), 4)

def updateMinute(value):
    canvas.delete(tags[3])
    printDigit(value%10, 3)
    if value%10 == 0:
        canvas.delete(tags[2])
        printDigit((int)(value/10), 2)


def updateHour(value):
    canvas.delete(tags[1])
    printDigit(value%10, 1)
    if value%10 == 0:
        canvas.delete(tags[0])
        printDigit((int)(value/10), 0)

update()


def on_closing():
    global stop
    stop = True
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()