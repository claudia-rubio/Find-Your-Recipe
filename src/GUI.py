#this file contains basic GUI Stuff
import tkinter as tk
from tkinter import Text
from Recipe import readData

recipes = readData()

def submitButton(time, c, d, ni, ing, sort_type):
    if time.isdigit():
        recipes[0].time_input = int(time)
    if c.isdigit():
        recipes[0].calories_input = int(c)
    if ni.isdigit():
        recipes[0].ni_input = int(ni)
    if d == 'E':
        recipes[0].difficulty_input = 1
    elif d == 'H':
        recipes[0].difficulty_input = 26
    myFunct()

def myFunct():
    for i in range(3):
        recipes[i].calculate_search_factor()
        recipes[i].print_recipe()
        print(recipes[i].searchFactor)


xpos = 0.17
root = tk.Tk()
greenILike = '#93c47d'

#background 
canvas = tk.Canvas(root, height=500, width=850)
canvas.pack()
frame = tk.Frame(root, bg=greenILike)
frame.place(relwidth=1, relheight=1)

#title Label
label = tk.Label(frame, text="FIND YOUR RECIPE", font=('Helvetica',30,'bold'), bg=greenILike)
label.place(relx=0.26, rely =0.07)

#Left-hand side labels
label1 = tk.Label(frame, text="Cooking time:", font=30, bg=greenILike)
label1.place(relx=xpos, rely=0.32)

label2 = tk.Label(frame, text="Calories:", font=30, bg=greenILike)
label2.place(relx=xpos, rely =0.42)

label3 = tk.Label(frame, text="Difficulty:", font=30, bg=greenILike)
label3.place(relx=xpos, rely =0.52)

#Left-hand side entries
entry1 = tk.Entry(frame)
entry1.place(relx=xpos+0.15, rely=0.33, width = 60)

entry2 = tk.Entry(frame)
entry2.place(relx=xpos+0.15, rely=0.43, width = 60)

entry3 = tk.Entry(frame)
entry3.place(relx=xpos+0.15, rely=0.53, width = 60)


#right-hand side labels
label4 = tk.Label(frame, text="Number of\nIngredients:", font=30, bg=greenILike)
label4.place(relx=0.5, rely=0.31)

label5 = tk.Label(frame, text="Specific\nIngredient:", font=30, bg=greenILike)
label5.place(relx=0.5, rely=0.47)

#right-hand side entry
entry4 = tk.Entry(frame)
entry4.place(relx=0.63, rely=0.37, width = 60)

entry5 = tk.Entry(frame)
entry5.place(relx=0.63, rely=0.52, width=150)

#buttons
button1 = tk.Button(frame, text="Sort best matches \nusing Quick Sort", bg='yellow', command=lambda: submitButton(entry1.get(), entry2.get(),
                                                                                                    entry3.get(), entry4.get(), entry5.get(), True))
button1.place(relx=0.29, rely=0.83)

label6 = tk.Label(frame, text="OR", font=('Helvetica',15,'bold'), bg=greenILike)
label6.place(relx=0.48, rely =0.83)

button2 = tk.Button(frame, text="Sort best matches \nusing Merge Sort", bg='yellow', command=lambda: submitButton(entry1.get(), entry2.get(),
                                                                                                    entry3.get(), entry4.get(), entry5.get(), False))
button2.place(relx=0.60, rely=0.83)

root.mainloop()