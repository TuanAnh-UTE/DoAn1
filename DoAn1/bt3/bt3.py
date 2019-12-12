
from tkinter import *
from tkinter import ttk
import threading
import math
import time

win_width = 200
win_heigh = 200
geometry = "%dx%d" % (win_width,win_heigh)

circlex = win_width/8*3 # tam hinh tron lon
circley = win_heigh/2
R = 50                  # ban kinh hinh tron lon

pointx = circlex+R      # tam hinh tron nho
pointy = circley        
Rpoint = 5              # ban kinh hinh tron nho
angle = 0               # goc tinh tam hinh tron nho

step = math.pi/100     
updatetime = 0.02      # thoi gian update

def update(e, event):
    global b, c, circlex, circley, pointx, pointy, R, Rpoint, angle

    while 1:
        e.wait()
        if event.isSet():
            break

        angle -= step
        pointx = math.cos(angle)*R + circlex
        pointy = math.sin(angle)*R + circley

        canvas.delete("point")
        canvas.create_oval(pointx-Rpoint, pointy-Rpoint, pointx+Rpoint, pointy+Rpoint, fill="red", tag="point")
        time.sleep(updatetime)


e = threading.Event()               # cờ để bắt đầu chạy
stopevent = threading.Event()       # cờ để tắt thread khi tắt cửa sổ
def start():
    global e
    e.set()

def stop():
    global e
    e.clear()

root = Tk()
root.title("BT3")
# root.geometry(geometry)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

canvas = Canvas(root, width=win_width/4*3, height=win_heigh)
canvas.grid(column=0, row=0)
canvas.create_oval(circlex-R, circley-R, circlex+R, circley+R, width=3 )

canvas.create_oval(pointx-Rpoint, pointy-Rpoint, pointx+Rpoint, pointy+Rpoint, fill="red", tag="point")

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=1, row=0, sticky=(N, W, E, S))

btnstart = Button(frame, text="start", command=start)
btnstart.pack(fill = BOTH)

btnstop = Button(frame, text="stop", command=stop)
btnstop.pack(fill = BOTH)

t = threading.Thread(target=update,
                     args=(e,stopevent, ))
t.start()

def on_closing():
    global stopevent, t
    stopevent.set()
    e.set()
    t.join()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()