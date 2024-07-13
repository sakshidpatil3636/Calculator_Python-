from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("360x600")
root.title("Calculator")
root.resizable(0,0)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", borderwidth=6, relief=SUNKEN )
screen.pack(fill=X, ipadx=1, pady=4, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=20, pady=2,font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="3", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="-", padx=25, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=23, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="/", padx=25, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=16, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=20, pady=2, font="lucida 35 bold", bg = "light blue")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)

f.pack()



root.mainloop()
