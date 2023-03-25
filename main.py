from tkinter import *

window = Tk()
window.wm_title("3D Printer Machine Management")

l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l1 = Label(window, text="Manufacturer")
l1.grid(row=1, column=0)

l1 = Label(window, text="Model")
l1.grid(row=1, column=2)

l1 = Label(window, text="Serial Number")
l1.grid(row=2, column=0)

l1 = Label(window, text="Firmware Version")
l1.grid(row=2, column=2)

l1 = Label(window, text="Calibration")
l1.grid(row=3, column=0)

l1 = Label(window, text="Year")
l1.grid(row=3, column=2)

name = StringVar()
ent1 = Entry(window, textvariable = title_text)
ent1.grid(row=0, column=1)

manufacturer = StringVar()
ent2 = Entry(window, textvariable = title_text)
ent2.grid(row=1, column=1)

model = StringVar()
ent3 = Entry(window, textvariable = title_text)
ent3.grid(row=1, column=3)

serial_num = StringVar()
ent4 = Entry(window, textvariable = title_text)
ent4.grid(row=2, column=1)

firmware_vers = StringVar()
ent5 = Entry(window, textvariable = title_text)
ent5.grid(row=2, column=3)

title_text = StringVar()
ent6 = Entry(window, textvariable = title_text)
ent6.grid(row=3, column=1)

title_text = StringVar()
ent7 = Entry(window, textvariable = title_text)
ent7.grid(row=3, column=3)

window.mainloop()