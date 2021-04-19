#this file contains basic GUI Stuff
import tkinter as tk
from tkinter import *
from tkscrolledframe import ScrolledFrame
from Recipes import Recipes
from Recipe import Recipe
from Recipes import mergeSort
import time

greenILike = '#93c47d'
recipe_list = Recipes()
cook_book = recipe_list.recipes


#this function takes the user input, and update how the  
#search factor of each recipe will be calculated
#if there's input for the ingredient section then the list will be filtered
#and then sorted
def submitButton(t, c, d, ni, ing, sort_type, root):
    if len(ing) > 1:
        recipe_list.search_ingredient(ing.lower())

    if t.isdigit():
        Recipe.time_input = int(t)
    else:
        Recipe.time_input = False

    if c.isdigit():
        Recipe.calories_input = int(c)
    else:
        Recipe.calories_input = False

    if ni.isdigit():
        Recipe.ni_input = int(ni)
    else:
        Recipe.ni_input = False

    if d == 'E':
        Recipe.difficulty_input = 1
    elif d == 'H':
        Recipe.difficulty_input = 26
    else:
        Recipe.difficulty_input = False

    start_time = time.time()
    
    if sort_type == True:
        mergeSort(recipe_list.recipes)
    else:
        recipe_list.heapSort()

    end_time = time.time()
    
    draw_frame_2(end_time - start_time, root)

    
#this draws the second screen with the results from the sorting
def draw_frame_2(elapsed_time, root):
    sf = ScrolledFrame(root, bg=greenILike)
    sf.place(relwidth =1, relheight =1)

    sf.bind_arrow_keys(root)
    sf.bind_scroll_wheel(root)

    frame2 = sf.display_widget(Frame, bg=greenILike)
    
    l = tk.Label(frame2, text = "Sorted Results" , font=('Helvetica',30,'normal'), bg=greenILike)
    st = "Time taken:  " + str(elapsed_time)
    l1 = tk.Label(frame2, text = st, font=('Helvetica', 15, "normal"), bg = greenILike)
    l.grid(row = 0, column = 1, columnspan = 4)
    l1.grid(row = 1, column = 1, columnspan = 4)

    tk.Label(frame2, padx = 20, text = "Name", font =('Helvetica', 12, 'bold'), bg =greenILike).grid(row = 2, column = 0, pady = 2, sticky = 'w')
    tk.Label(frame2, text = "Time",  font =('Helvetica', 12, 'bold'), bg =greenILike).grid(row = 2, column =2, pady = 2)
    tk.Label(frame2, padx = 10, text = "Calories",  font =('Helvetica', 12, 'bold'), bg =greenILike).grid(row = 2, column =3, pady = 2)
    tk.Label(frame2, padx = 10, text = "Steps", font =('Helvetica', 12, 'bold'), bg = greenILike).grid(row=2, column =4, pady =2)
    tk.Label(frame2, padx = 10, text = "No Ingredients", font =('Helvetica', 12, 'bold'), bg = greenILike).grid(row=2, column =5, pady =2)
    tk.Label(frame2, padx = 20, text = "Ingredients",  font =('Helvetica', 12, 'bold'), bg =greenILike).grid(row = 2, column =6, columnspan = 2, pady = 2, sticky = 'w')
    for i in range(3, min(len(recipe_list.recipes)-1, 300)):
        tk.Label(frame2, padx = 20, text = recipe_list.recipes[i-3].name,  bg=greenILike).grid(row = i, column =0, columnspan = 2, pady = 2, sticky = 'w')
        tk.Label(frame2, text = str(recipe_list.recipes[i-3].minutes),  bg=greenILike).grid(row = i, column =2, pady = 2)
        tk.Label(frame2, text = str(recipe_list.recipes[i-3].calories),  bg=greenILike).grid(row = i, column =3, pady = 2)
        tk.Label(frame2, text = str(recipe_list.recipes[i-3].n_s), bg = greenILike).grid(row =i, column = 4, pady=2)
        tk.Label(frame2, text = str(recipe_list.recipes[i-3].n_i), bg = greenILike).grid(row =i, column = 5, pady=2)
        tk.Label(frame2, padx = 20, text = recipe_list.recipes[i-3].ing_info(),  bg=greenILike).grid(row = i, column =6, columnspan = 2, pady = 2, sticky = 'w')

    button3 = tk.Button(frame2, text="GO BACK", bg='yellow', command=lambda: goBack(root))
    button3.grid(row=0, column=5)
    
def goBack(root):
    draw_frame_1(root)


def draw_frame_1(root):
    recipe_list.recipes = cook_book.copy() #make sure size of list is not shrinked when re-entering main menu
    xpos = 0.17
    frame = tk.Frame(root, bg=greenILike)
    frame.place(relwidth=1, relheight=1)

    #title Label
    label = tk.Label(frame, text="FIND YOUR RECIPE", font=('Helvetica',30,'bold'), bg=greenILike)
    label.place(relx=0.33, rely =0.07)

    #Left-hand side labels
    label1 = tk.Label(frame, text="Cooking time (mins):", font=('Helvetica',18,'normal'), bg=greenILike)
    label1.place(relx=xpos, rely=0.32)

    label2 = tk.Label(frame, text="Calories:", font=('Helvetica',18,'normal'), bg=greenILike)
    label2.place(relx=xpos, rely =0.42)

    label3 = tk.Label(frame, text="Difficulty (E/H):", font=('Helvetica',18,'normal'), bg=greenILike)
    label3.place(relx=xpos, rely =0.52)

    #Left-hand side entries
    entry1 = tk.Entry(frame)
    entry1.place(relx=xpos+0.21, rely=0.33, width = 60)

    entry2 = tk.Entry(frame)
    entry2.place(relx=xpos+0.21, rely=0.43, width = 60)

    entry3 = tk.Entry(frame)
    entry3.place(relx=xpos+0.21, rely=0.53, width = 60)


    #right-hand side labels
    label4 = tk.Label(frame, text="Number of\nIngredients:", font=('Helvetica',18,'normal'), bg=greenILike)
    label4.place(relx=0.6, rely=0.31)

    label5 = tk.Label(frame, text="Specific\nIngredient:", font=('Helvetica',18,'normal'), bg=greenILike)
    label5.place(relx=0.6, rely=0.47)

    #right-hand side entry
    entry4 = tk.Entry(frame)
    entry4.place(relx=0.73, rely=0.34, width = 60)

    entry5 = tk.Entry(frame)
    entry5.place(relx=0.73, rely=0.50, width=150)

    #buttons
    button1 = tk.Button(frame, text="Sort best matches \nusing Merge Sort", font=('Helvetica',15,'normal'), bg='yellow', command=lambda: submitButton(entry1.get(), entry2.get(),
                                                                                                        entry3.get(), entry4.get(), entry5.get(), True, root))
    button1.place(relx=0.20, rely=0.83)

    label6 = tk.Label(frame, text="OR", font=('Helvetica',15,'bold'), bg=greenILike)
    label6.place(relx=0.43, rely =0.83)

    button2 = tk.Button(frame, text="Sort best matches \nusing Heap Sort", font=('Helvetica',15,'normal'), bg='yellow', command=lambda: submitButton(entry1.get(), entry2.get(),
                                                                                                        entry3.get(), entry4.get(), entry5.get(), False, root))
    button2.place(relx=0.55, rely=0.83)

def main():
    
    root = tk.Tk()
    canvas = tk.Canvas(root, height=700, width=1150)
    canvas.pack()

    draw_frame_1(root)
    root.mainloop()

if __name__ == "__main__":
    main()

