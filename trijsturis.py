import math
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.config(bg='#7b70b5')
head = Label(root, text="Izveido savu trijstūri!", background='#7b70b5',).place(x=250, y=50)
tri = Canvas(root, width=200, height=200, highlightthickness=0, borderwidth=0)
tri.place(x=200, y=100)
bg = tri.create_rectangle(2,2,198,198, outline= 'black', width=4, fill='#aeb0ae')
mala1 = Label(root, text="1. mala", bg='#7b70b5').place(x=30, y=120)
mala2 = Label(root, text="2. mala", bg='#7b70b5').place(x=30, y=170)
mala3 = Label(root, text="3. mala", bg='#7b70b5').place(x=30, y=220)
mal1 = Entry(root, width=10)
mal1.place(x=90, y=120)
mal2 = Entry(root, width=10)
mal2.place(x=90, y=170)
mal3 = Entry(root, width=10)
mal3.place(x=90, y=220)
def check1():
    x = int(mal1.get())
    y = int(mal2.get())
    z = int(mal3.get())
    try:
        print(x, y, z)
    except ValueError:
        print("is not a number")
    if x+y<z or x+z<y or y+z<x:
        messagebox.showerror('Python Error', 'Error: šis trijstūris nav iespējams!')
    # if x<z and y<z:
    #     x = z
    #     z = x
    # if x<y and z<y:
    #     x = y
    #     y = x
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    x = x*10
    y0 = 180
    x0 = 50
    r0 = y*10
    y1 = 180
    x1 = (x+50)
    r1 = z*10

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None

    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d
        y2=y0+a*(y1-y0)/d
        x3=x2+h*(y1-y0)/d
        y3=y2-h*(x1-x0)/d

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        tri.delete('all')
        triangle = tri.create_polygon(x0, y0, x1, y1, x3, y3, fill= '#30c747', outline='black', width=4)

        print(d, a, h,'', x2, y2,' ', x3, y3," ", x4, y4)

bu = Button(root , width = 20,text="press",command=check1)
bu.place(x = 500 , y = 500)



# triangle = tri.create_polygon(20, 180, 20, 20, 180, 180, fill= '#30c747', outline='black', width=4)

mainloop()