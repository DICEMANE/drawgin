from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("drawing")
canv = Canvas(root, width=600, height=600, bg='grey')
canv.pack()
# room
ground1 = canv.create_line(0, 450, 600, 450, fill='#4f4f4e')
wall = canv.create_rectangle(0, 0, 602, 450, fill='#7a7a77')

# door1
door1 = canv.create_rectangle(0, 100, 100, 450, fill='#a33131', outline='#a33131')
door2 = canv.create_oval(70, 285, 90, 300, width=2, fill='#5e1919', outline='#5e1919')
# door2
door3 = canv.create_rectangle(500, 100, 601, 450, fill='#a33131', outline='#a33131')
door4 = canv.create_oval(510, 285, 530, 300, width=2, fill='#5e1919', outline='#5e1919')
mainloop()
