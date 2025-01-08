from tkinter import *

root = Tk()

root.title('Simple calculator')

e = Entry(root, width=35, borderwidth = 5)
e.grid(row=0, column=0, columnspan=3)


def button_clear():
    e.delete(0, END)


def click_button(symbol):
    e.get()
    e.insert('end', symbol)

'''
def button_add ():
  global first_number
  first_number = e.get()
  

def button_equal():
    global first_number
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, str(int(first_number) + int(second_number))) '''

def button_add():
  global first_number
  first_number = e.get()

def button_equal():
  global first_number  # Add this line
  second_number = e.get()
  e.delete(0, END)
  e.insert(0, str(int(first_number) + int(second_number)))  # Convert to int, add, then convert



#creating buttons
button1 = Button(root, text ='1', padx=40, pady=10, command = lambda: click_button(1))
button2 = Button(root, text = '2', padx=40, pady=10, command = lambda: click_button(2))
button3 = Button(root, text ='3', padx=40, pady=10, command = lambda: click_button(3))
button4 = Button(root, text ='4', padx=40, pady=10, command = lambda: click_button(4))
button5 = Button(root, text ='5', padx=40, pady=10, command = lambda: click_button(5))
button6 = Button(root, text ='6', padx=40, pady=10, command = lambda: click_button(6))
button7 = Button(root, text ='7', padx=40, pady=10, command = lambda: click_button(7))
button8 = Button(root, text ='8', padx=40, pady=10, command = lambda: click_button(8))
button9 = Button(root, text ='9',  padx=40, pady=10, command = lambda: click_button(9))
button0 = Button(root, text ='0',  padx=40, pady=10, command = lambda: click_button(0))
button_add = Button(root, text ='+', padx=39, pady=10, command =lambda: click_button('+'))
'''button_subtract = Button(root, text = '-', padx=42, pady=10, command = button_subtract)
button_division = Button(root, text='/', padx=42, pady=10, command = button_divide)
button_multiplication = Button(root, text = '*', padx=40, pady=10, command = button_multiply)'''
button_equal = Button(root, text = '=', padx = 87, pady=10, command = button_equal)
button_clear = Button( root, text = 'Clear', padx=76, pady=10, command = button_clear)

#displayong buttons
button1.grid(row =3, column = 0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row =2, column = 0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row =1, column = 0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row =4, column = 0)

button_add.grid(row=5, column=0)
'''button_subtract.grid(row=6, column=0)
button_division.grid(row =6, column = 1)
button_multiplication.grid(row=6, column=2)'''

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row =5, column = 1, columnspan=2)




root.mainloop()
