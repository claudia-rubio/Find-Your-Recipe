#this file contains basic GUI Stuff
import tkinter as tk
from tkinter import Text
from Recipes import Recipes

recipe_list = Recipes()

#this function takes the user input, and update how the 
#search factor of each recipe is calculated
#if there's input for the ingredient section then the list will be filtered
#and then sorted
def submitButton(time, c, d, ni, ing, sort_type):
    if len(ing) > 1:
        recipe_list.search_ingredient(ing)

    if time.isdigit():
        recipe_list.recipes[0].time_input = int(time)
    else:
        recipe_list.recipes[0].time_input = False

    if c.isdigit():
        recipe_list.recipes[0].calories_input = int(c)
    else:
        recipe_list.recipes[0].calories_input = False

    if ni.isdigit():
        recipe_list.recipes[0].ni_input = int(ni)
    else:
        recipe_list.recipes[0].ni_input = False

    if d == 'E':
        recipe_list.recipes[0].difficulty_input = 1
    elif d == 'H':
        recipe_list.recipes[0].difficulty_input = 26
    else:
        recipe_list.recipes[0].difficulty_input = False
    
    myFunct()

def myFunct():
    for i in range(3):
        recipe_list.recipes[i].calculate_search_factor()
        recipe_list.recipes[i].print_recipe()
        print(recipe_list.recipes[i].searchFactor)


#the following is user interface 

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