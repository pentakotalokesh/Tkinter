from tkinter import *

import sys

import time

def times():
	current_time = time.strftime("%H:%M:%S")
	clock.config(text = current_time)
	clock.after(200,times)

window = Tk()

window.geometry("500x250")
window.config(background = "green")
clock = Label(window,font = ("times",50,'bold'),bg = 'white')
clock.grid(row = 2,column = 2,padx = 100,pady = 25)

dighead = Label (window,text = "Digital Clock",font = ("times",20,'bold'))
dighead.grid(row = 0,column=2,padx = 90,pady = 25)
times()
window.mainloop()