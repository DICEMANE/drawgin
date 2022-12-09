from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("drawing")
canv = Canvas(root, width=600, height=600, bg='grey')
canv.pack()
# room
ground1 = canv.create_line(0, 450, 600, 450, fill='#4f4f4e')
wall = canv.create_rectangle(0, 0, 602, 450, fill='#7a7a77')
# table
table2 = canv.create_line(450, 500, 450, 335, width=30, fill='#821811')
table3 = canv.create_line(150, 500, 150, 335, width=30, fill='#821811')
table1 = canv.create_line(135, 350, 465, 350, width=30, fill='brown')
# lamp
lamp1 = canv.create_line(170, 330, 230, 330, width=10, fill='#5c5857')
lamp2 = canv.create_line(170, 270, 200, 330, width=4, fill='#5c5857')
lamp3 = canv.create_line(250, 240, 170, 270, width=4, fill='#5c5857')
lamp4 = canv.create_polygon(250, 238, 238, 280, 285, 263, width=4, fill='#5c5857')
lamp5 = canv.create_oval(170, 268, 177, 275, width=2, fill='#5c5857')
lamp6 = canv.create_arc(252, 281, 272, 261, start=200, extent=180, fill="#9ba688")
lamp7 = canv.create_rectangle(220, 400, 240, 420, fill='#c5c7c5')
lamp8 = canv.create_line(226, 405, 226, 411)
lamp9 = canv.create_line(234, 405, 234, 411)
lamp10 = canv.create_arc(227, 414, 233, 414, start=200, extent=180)
# book
book1 = canv.create_line(270, 327, 335, 327, width=15, fill='green')
# door1
doorhandle1 = Button(borderwidth=0, height=1, width=1, bg='#818581', activebackground='#818581')
doorhandle1.place(x=75, y=290)
door1 = canv.create_rectangle(0, 100, 100, 450, fill='#a33131', outline='#a33131')

# door2
door3 = canv.create_rectangle(500, 100, 601, 450, fill='#a33131', outline='#288541')
door4 = canv.create_oval(510, 285, 530, 300, width=2, fill='#5e1919', outline='#5e1919')
mainloop()
