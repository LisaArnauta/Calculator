from tkinter import *


root = Tk()
root.title('Calculator')



#entry field
input_num = Entry(root, width=47, borderwidth=10, bg='#DAF7A6')



def button_add():
    first_number = input_num.get()
    global f_num  # we put here global variable to use it in other function (equal)
    global operation # and here we put global variable to use it as test conditions in equal function
    operation = 'addition'
    f_num = int(first_number)
    input_num.delete(0, END)

def button_multiply():
    first_number = input_num.get()
    global first_num
    global operation
    operation = 'multiplication'
    f_num = int(first_number)
    input_num.delete(0, END)

def button_divide():
    first_number = input_num.get()
    global f_num
    global operation
    operation = 'division'
    f_num = int(first_number)
    input_num.delete(0, END)


def button_subtract():
    first_number = input_num.get()
    global f_num
    global operation
    operation = 'subtraction'
    f_num = int(first_number)
    input_num.delete(0, END)

def button_elevate():
    first_number = input_num.get()
    global f_num
    global operation
    operation = 'elevation'
    f_num = int(first_number)
    input_num.delete(0, END)

def button_root():
    first_number = input_num.get()
    global f_num
    global operation
    operation = 'root'
    f_num = int(first_number)
    input_num.delete(0, END)


def click(number):
    current = input_num.get()
    input_num.delete(0, END)
    input_num.insert(0, str(number) + str(current))

def clear_ths():
    input_num.delete(0, END)

def button_equal():
    second_number = input_num.get()
    input_num.delete(0, END)

    if operation == 'addition':
        input_num.insert(0, f_num + int(second_number))
    if operation == 'division':
        input_num.insert(0, f_num / int(second_number))
    if operation == 'multiplication':
        input_num.insert(0, f_num * int(second_number))
    if operation == 'subtraction':
        input_num.insert(0, f_num - int(second_number))
    if operation == 'elevation':
        input_num.insert(0, f_num ** int(second_number))
    if operation == 'root':
        input_num.insert(0, f_num ** (1/(int(second_number))))



# Here all buttons we used ->

button_7 = Button(root, text='7', padx=42, pady=20, command=lambda: click(7), bg='#FF5733' )
button_8 = Button(root, text='8', padx=42, pady=20, command=lambda: click(8), bg='#FF5733')
button_9 = Button(root, text='9', padx=42, pady=20, command=lambda: click(9), bg='#FF5733')
button_4 = Button(root, text='4', padx=42, pady=20, command=lambda: click(4), bg='#FF5733')
button_5 = Button(root, text='5', padx=42, pady=20, command=lambda: click(5), bg='#FF5733')
button_6 = Button(root, text='6', padx=42, pady=20, command=lambda: click(6), bg='#FF5733')
button_1 = Button(root, text='1', padx=42, pady=20, command=lambda: click(1), bg='#FF5733')
button_2 = Button(root, text='2', padx=42, pady=20, command=lambda: click(2), bg='#FF5733')
button_3 = Button(root, text='3', padx=42, pady=20, command=lambda: click(3), bg='#FF5733')
button_0 = Button(root, text='0', padx=42, pady=20, command=lambda: click(0), bg='#FF5733')
button_add = Button(root, text='+', padx=42, pady=20, command=button_add, bg='#52914A')
button_clear = Button(root, text='CE', padx=40.5, pady=20, command=clear_ths, bg='#52914A')
button_equal = Button(root, text='=', padx=42, pady=20, command=button_equal, bg='#52914A')
button_multiply = Button(root, text='*', padx=42, pady=20, command=button_multiply, bg='#52914A')
button_divide = Button(root, text='/', padx=42, pady=20, command=button_divide, bg='#52914A')
button_subtract = Button(root, text='-', padx=42, pady=20, command=button_subtract, bg='#52914A')
button_elevate = Button(root, text='^', padx=42, pady=20, command=button_elevate, bg='#52914A')
button_root = Button(root, text='√', padx=42, pady=20, command=button_root, bg='#52914A')




# put all these buttons as grid ->
input_num.grid(row=0, column=0, columnspan=5, padx=10, pady=1)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=6, column=2)
button_equal.grid(row=6, column=1)

button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_subtract.grid(row=6, column=0)
button_elevate.grid(row=5, column=1)
button_root.grid(row=5, column=2)



root.mainloop()



