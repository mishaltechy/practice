from tkinter import *

window = Tk(className='Calculator')
window.geometry('320x503+550+100')
window.configure(bg='black')

text_in = StringVar()
operator = ""
checker = ""

def button_click(number):
    global operator
    text_in.set(operator)
    operator = operator + str(number)
    text_in.set(operator)


def back_button_click():
    global operator
    text_in.set(operator)
    operator = operator[:-1]
    text_in.set(operator)


def clear_button_click():
    global operator
    operator = ' '
    text_in.set(operator)


def undefined_button_click():
    text_in.set('undefined')


def plus_button_click():
    global checker
    global operator
    global old_String
    old_String = str(text_in.get()).encode()
    operator = ' '
    checker = 1
    text_in.set(operator)


def minus_button_click():
    global operator,checker
    global old_String
    old_String = str(text_in.get()).encode()
    operator = ' '
    checker = 2
    text_in.set(operator)


def multiple_button_click():
    global checker
    global operator
    global old_String
    old_String = str(text_in.get()).encode()
    operator = ' '
    checker = 3
    text_in.set(operator)


def division_button_click():
    global checker
    global operator
    global old_String
    old_String = str(text_in.get()).encode()
    operator = ' '
    checker = 4
    text_in.set(operator)


def equal_button_click():
    try:
        global new_String
        global operator
        new_String = str(text_in.get()).encode()
        if checker == 1 :
            operator = (+float(old_String)) + (+float(new_String))
        elif checker == 2 :
            operator = (+float(old_String)) - (+float(new_String))
        elif checker == 3 :
            operator = (+float(old_String)) * (+float(new_String))
        elif checker == 4 :
            operator = (+float(old_String)) / (+float(new_String))
        text_in.set(float(operator))
    except:
        operator = " Error "
        text_in.set(operator)


displayLabel = Label(window, font=("Helvatical bold", 25), textvar=text_in, width=16, height=5, bg='BLACK', fg='white',
                     anchor=E)
displayLabel.pack()

zero_button = Button(window, text='0', padx=24, pady=10, command=lambda: button_click(0), bg='black', fg='white')
zero_button.configure(font=('Helvatical bold', 14))
zero_button.place(x=85, y=440)

one_button = Button(window, text='1', padx=24, pady=10, command=lambda: button_click(1), bg='black', fg='white')
one_button.configure(font=('Helvatical bold', 14))
one_button.place(x=8, y=380)

two_button = Button(window, text='2', padx=24, pady=10, command=lambda: button_click(2), bg='black', fg='white')
two_button.configure(font=('Helvatical bold', 14))
two_button.place(x=85, y=380)

three_button = Button(window, text='3', padx=24, pady=10, command=lambda: button_click(3), bg='black', fg='white')
three_button.configure(font=('Helvatical bold', 14))
three_button.place(x=162, y=380)

four_button = Button(window, text='4', padx=24, pady=10, command=lambda: button_click(4), bg='black', fg='white')
four_button.configure(font=('Helvatical bold', 14))
four_button.place(x=8, y=320)

five_button = Button(window, text='5', padx=24, pady=10, command=lambda: button_click(5), bg='black', fg='white')
five_button.configure(font=('Helvatical bold', 14))
five_button.place(x=85, y=320)

six_button = Button(window, text='6', padx=24, pady=10, command=lambda: button_click(6), bg='black', fg='white')
six_button.configure(font=('Helvatical bold', 14))
six_button.place(x=162, y=320)

seven_button = Button(window, text='7', padx=24, pady=10, command=lambda: button_click(7), bg='black', fg='white')
seven_button.configure(font=('Helvatical bold', 14))
seven_button.place(x=8, y=260)

eight_button = Button(window, text='8', padx=24, pady=10, command=lambda: button_click(8), bg='black', fg='white')
eight_button.configure(font=('Helvatical bold', 14))
eight_button.place(x=85, y=260)

nine_button = Button(window, text='9', padx=24, pady=10, command=lambda: button_click(9), bg='black', fg='white')
nine_button.configure(font=('Helvatical bold', 14))
nine_button.place(x=162, y=260)

dot_button = Button(window, text='.', padx=27, pady=10, command=lambda: button_click("."), bg='black', fg='white')
dot_button.configure(font=('Helvatical bold', 14))
dot_button.place(x=162, y=440)

clear_button = Button(window, text='AC', padx=16, pady=10, command=clear_button_click, bg='#2F4F4F', fg='white')
clear_button.configure(font=('Helvatical bold', 14))
clear_button.place(x=8, y=200)

back_button = Button(window, text='DC', padx=16, pady=10, bg='#2F4F4F', command=lambda: back_button_click(), fg='white')
back_button.configure(font=('Helvatical bold', 14))
back_button.place(x=85, y=200)

plusOminus_button = Button(window, text='+/-', padx=19, pady=10, command=undefined_button_click, bg='#2F4F4F',
                           fg='white')
plusOminus_button.configure(font=('Helvatical bold', 14))
plusOminus_button.place(x=162, y=200)

percentage_button = Button(window, text='%', padx=21, pady=10, command=undefined_button_click, bg='black',
                           fg='white')
percentage_button.configure(font=('Helvatical bold', 14))
percentage_button.place(x=8, y=440)

mc_button = Button(window, text='mc', padx=17, pady=4, command=undefined_button_click, bg='#2F4F4F', fg='white')
mc_button.configure(font=('italic', 14))
mc_button.place(x=8, y=153)

mPlus_button = Button(window, text='m+', padx=16, pady=4, command=undefined_button_click, bg='#2F4F4F', fg='white')
mPlus_button.configure(font=('Helvatical bold', 14))
mPlus_button.place(x=85, y=153)

mMinus_button = Button(window, text='m-', padx=19, pady=4, command=undefined_button_click, bg='#2F4F4F', fg='white')
mMinus_button.configure(font=('Helvatical bold', 14))
mMinus_button.place(x=162, y=153)

mr_button = Button(window, text='mr', padx=20, pady=4, command=undefined_button_click, bg='#2F4F4F', fg='white')
mr_button.configure(font=('Helvatical bold', 14))
mr_button.place(x=239, y=153)

plus_button = Button(window, text='+', padx=24, pady=10, command=plus_button_click, bg='#2F4F4F', fg='white')
plus_button.configure(font=('Helvatical bold', 14))
plus_button.place(x=239, y=380)

minus_button = Button(window, text='-', padx=27, pady=10, command= minus_button_click, bg='#2F4F4F', fg='white')
minus_button.configure(font=('Helvatical bold', 14))
minus_button.place(x=239, y=320)

multiple_button = Button(window, text='x', padx=26, pady=10, command=multiple_button_click, bg='#2F4F4F', fg='white')
multiple_button.configure(font=('Helvatical bold', 14))
multiple_button.place(x=239, y=260)

division_button = Button(window, text='/', padx=28, pady=10, command=division_button_click, bg='#2F4F4F', fg='white')
division_button.configure(font=('Helvatical bold', 14))
division_button.place(x=239, y=200)

equal_button = Button(window, text='=', padx=24, pady=10, command=equal_button_click, bg='YELLOW', fg='black')
equal_button.configure(font=('Helvatical bold', 14))
equal_button.place(x=239, y=440)

window.mainloop()

