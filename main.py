import random
from tkinter import *
import tkinter as tk

# Window

window = Tk()
window.title('Password Generator')
window.geometry('500x200')
window.config(bg='#323232')
window.iconphoto(False, PhotoImage(file='C:/Users/User/Desktop/123.png'))

# Create the Password

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))

lowercase1 = chr(random.randint(97, 123))
lowercase2 = chr(random.randint(97, 123))
lowercase3 = chr(random.randint(97, 123))
lowercase4 = chr(random.randint(97, 123))

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)
number4 = random.randint(0, 9)

symbol1 = chr(random.randint(33, 47))
symbol2 = chr(random.randint(33, 47))
symbol3 = chr(random.randint(33, 47))
symbol4 = chr(random.randint(33, 47))


password = str(uppercase1) + str(uppercase2) + str(lowercase1) + str(lowercase2) + str(lowercase3) + str(lowercase4) + str(number1) + str(number2) + str(number3) + str(number4) + str(symbol1) + str(symbol2) + str(symbol3) + str(symbol4)
password = shuffle(password)

# Generator Button

def password_generator():
    screen.delete(0, END)
    screen.insert(0, password)

# Inside Window

label_title = Label(window, text='Password Generator', fg='#992E00', font=('Showcard Gothic', 20, 'bold'), bg='#323232')
label_title.pack(side=TOP)

givespace = Label(window, text='', bg='#323232')
givespace.pack()

screen = Entry(window, width=40, borderwidth=5)
screen.pack()

givespace1 = Label(window, text='', bg='#323232')
givespace1.pack()

generate_button = Button(window, text='Generate', bg='#992E00', fg='#323232', font=('Kristen ITC', 13), command=password_generator)
generate_button.pack()



window.mainloop()