from tkinter import *
from PIL import ImageTk,Image
import random

window = Tk()

window.title("GAME")
window.geometry("700x700")
window.config(background = "#2C2554")
HeadLabel =  Label(window,text="GUESS THE NUMBER",font = ("Monospace bold",20),bd = 30,bg = '#2C2554' ,fg = '#A81367')
HeadLabel.pack()
subhead = Label(window,text = "Enter any number from 1 - 10",bd = 20,bg = '#2C2554',fg = '#1397A8' )
subhead.pack()
entrybox = Entry(window,bd = 10)
entrybox.pack(ipadx = 7,ipady =5)
a_head = Label(window,text = "ONLY THREE ATTEMPTS WILL BE ALLOWED",bd = 10,bg = '#2C2554',fg = '#ff0000')
a_head.pack()
global output
global attempt
output = Label(window,text = "")
global canvas
global img

# Empty Canvas Declaration

canvas = Canvas( window,
                width = 300, 
                height = 250
                      )  
canvas.pack()
img = PhotoImage(file='logobasic.png')      
canvas.create_image(
                       10,
                       10, 
                anchor=NW, 
                image=img
   )  


#Function to clear last output
def clear_widget(widget):
    widget.destroy()
attempt = 1
# Function defenition for Button Command
def Check_number(num):
    entrybox.delete(0,END)
    global attempt
    attempt +=1
    if attempt <=4:
        temp = random.randint(1,10)
        print(temp)
        global output
        global canvas
        global img
        if int(num) == temp:
            clear_widget(output)
            clear_widget(canvas)
            output = Label(window,text = "YAY !! YOU GUESSED CORRECTLY",font = ("sans-serif bold",20),bg='#2C2554',fg='#ff0000')
            output.pack()
            canvas = Canvas(
                      window,
                      width = 600, 
                      height = 300
                      )  
            canvas.pack()
            img = PhotoImage(file='logo.png')      
            canvas.create_image(
                       10,
                       10, 
                anchor=NW, 
                image=img
                   )  
        else:
            clear_widget(output)
            clear_widget(canvas)
            output = Label(window,text = "OOPS !! YOU GUESSED WRONG NUMBER",font = ("sans-serif bold",20),bg='#2C2554',fg='#ff0000')
            output.pack()
            canvas = Canvas(
                      window,
                      width = 400, 
                      height = 300
                      )  
            canvas.pack()
            img = PhotoImage(file='logou.png')      
            canvas.create_image(
                       10,
                       10, 
                anchor=NW, 
                image=img
                   )      
    else:
        clear_widget(output)
        clear_widget(canvas)
        canvas = Canvas( window,
                width = 300, 
                height = 250
                      )  
        canvas.pack()
        img = PhotoImage(file='logofail1.png')      
        canvas.create_image(
                       10,
                       10, 
                anchor=NW, 
                image=img
        )  
        output = Label(window,text = "You Lost Your Attempts",font = ("Monospace bold",20),bg='#2C2554',fg = '#ff0000')
        output.pack()
    
    

sbutton = Button(window,text = "Check",command = lambda:Check_number(entrybox.get()),bd = 10)
sbutton.pack(padx=10,pady=10)
window.mainloop()