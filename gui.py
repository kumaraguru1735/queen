#!/usr/bin/python

import tkinter as tk

from PIL import ImageTk, Image

window = tk.Tk()

window.title("Queen")

window.geometry("900x900")

window.configure(background='grey')

path = "queen.png"

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")

window.mainloop()


