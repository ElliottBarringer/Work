import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random as rand

Window = tk.Tk()
Window.geometry("100x100")
Window.attributes('-topmost', True)

Background = tk.Toplevel()

w = Window.winfo_screenwidth()
h = Window.winfo_screenheight()

Background.geometry(f"{w}x{h}")
#Background.attributes('-topmost', True)
Background.configure(bg="black")
Background.resizable(False, False)
Background.overrideredirect(True)


mw = w//2
mh = h//2

screen_w = 100
screen_h = 100

Increase = 2

screen_w *= Increase
screen_h *= Increase

def ReBg(arg):

    Bg = tk.Tk()
    Bg.geometry(f"{w}x{h}")
    Bg.protocol("WM_DELETE_WINDOW", lambda arg=Bg: ReBg(arg))
    Bg.attributes('-topmost', True)
    Bg.configure(bg="black")

def Hydra(arg):

    n = 2

    for i in range(n):

        CreateWindow()

        n += 1

def CreateWindow():

    win = tk.Toplevel()
    win.geometry(f"{screen_w}x{screen_h}+{rand.randint(mw - 200, mw + 200)}+{rand.randint(mh - 200, mh + 200)}")
    win.title("Punishment")
    win.protocol("WM_DELETE_WINDOW", lambda arg=win: Hydra(arg))
    win.attributes('-topmost', True)

def BeginPunishment():

    Window.lift()

button = Button(Background, text="Commence Punishment", command=BeginPunishment)
button.pack()

Window.protocol("WM_DELETE_WINDOW", lambda arg=Window: Hydra(arg))
Background.protocol("WM_DELETE_WINDOW", lambda arg=Background: ReBg(arg))
Window.mainloop()