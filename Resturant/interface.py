from tkinter import *

window = Tk()
#Window Title
window.title("E-RESTAURANT")

#Window Dimensions
window.geometry("1024x720")

#Background Color
window.configure(background = "#005451")

#Content Heading
Heading = Label(window,text = "WELCOME TO PYTHON'S E-RESTAURANT",font=('Futura',30),padx = 50,pady = 50,bg = "#005451",fg = '#ffffff')
Heading.place(anchor = "center",relx = .5,rely = .1)

l=[]

list_of_items = Listbox(window,width = 50)

list_of_items.insert(100,"WADA                                              ₹100")
list_of_items.insert(50,"IDLI                                                  ₹50")
list_of_items.insert(250,"CHICKEN BIRIYANI                             ₹250")
list_of_items.insert(100,"SANDWICH                                       ₹100")
list_of_items.insert(300,"MUTTEN-BIRIYANI                             ₹300")
list_of_items.insert(30,"PANEER ROLL                                   ₹30")
list_of_items.insert(700,"STARTER PACK                                  ₹700")
list_of_items.insert(180,"VEG-BIRIYANI                                    ₹180")

global output
list_of_ordered_items = Listbox(window,width = 50)
# Functions - Working Procedures

# To Destroy Last Printed OUTPUT
def clear_widget(widget):
    widget.destroy()

# To Get List of Items
def list_Menu():
	global output
	output = Label(window,text = "***LIST OF ITEMS***",font = ('Arial',20),fg = "yellow",bg = "#005451")
	output.place(anchor="center",relx=.5,rely=.3)
	list_of_items.place(anchor="center",relx = .5,rely = .5)
                       

# To get an List of Ordered Items
def order_item():
	global output
	clear_widget(output)
	i = 1
	ele = list_of_items.get(ANCHOR)
	list_of_ordered_items.insert(i,ele)
#to Checkout the Bill Total Amount
def Check_out():
	global output
	clear_widget(list_of_items)
	clear_widget(output)
	list_of_ordered_items.place(anchor = "center",relx = .5,rely = .5)

#Menu-Card Button
button1 = Button(window,text="MENU-CARD",bg="Black",fg = "white",padx = 10,pady = 5,command = list_Menu)
button1.place(anchor = "e",relx = .3,rely = .2)

#Order Items Button
button2 = Button(window,text="ORDER-ITEMS",bg="Black",fg = "white",padx = 10,pady = 5,command = order_item)
button2.place(anchor = "center",relx = .5,rely = .2)
#Check-out
button2 = Button(window,text="CHECK-OUT",bg="Black",fg = "white",padx = 10,pady = 5,command = Check_out)
button2.place(anchor = "center",relx = .8,rely = .2)





window.mainloop()