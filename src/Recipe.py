import csv

def myFunct():
    print("hello")

class Recipe:
    #static variables
    time_input = False
    calories_input = False
    difficulty_input = False
    ni_input = False

    def __init__(self, n, min, cal, s, i):
        self.name = n
        self.minutes = min
        self.calories = cal
        self.n_s = s
        self.n_i = i
        self.searchFactor = 0
        self.ingredients = []

    def addIngredient(self, ing):
        self.ingredients.append(ing)

    def print_recipe(self):
        print("Name:      " + str(self.name))
        print("Minutes:   " + str(self.minutes))
        print("Calories:  " + str(self.calories))
        print("Ingredients  (" + str(self.n_i) + ") :")
        for item in self.ingredients:
            print("\t-" + item)

    #set static variables for comparison
    @property
    def time_input(self):
        return type(self)._time_input

    @time_input.setter
    def time_input(self,val):
        type(self)._time_input = val

    @property
    def difficulty_input(self):
        return type(self)._difficulty_input

    @difficulty_input.setter
    def difficulty_input(self,val):
        type(self)._difficulty_input = val

    @property
    def calories_input(self):
        return type(self)._calories_input

    @calories_input.setter
    def calories_input(self,val):
        type(self)._calories_input = val
        
    @property
    def ni_input(self):
        return type(self)._ni_input

    @ni_input.setter
    def ni_input(self,val):
        type(self)._ni_input = val

    #calculate recipe search factor
    def calculate_search_factor(self):
        if self.calories_input != False:
            self.searchFactor += abs(self.calories - self.calories_input)/700
        if self.ni_input != False:
            self.searchFactor += abs(self.n_i - self.ni_input)/9
        if self.time_input != False:
            self.searchFactor += abs(self.minutes - self.time_input)/120
        if self.difficulty_input != False:
            self.searchFactor += abs(self.n_s - self.difficulty_input)/9


#reads the information from the CSV file
def readData():
    recipes = []
    with open('src/dataset/recipes.CSV', newline='') as f:
        file = csv.reader(f)
        
        for line in file:
            #create new recipe
            new_recipe = Recipe(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]))
            #add its ingredients
            for ing in range(5, len(line)):
                #the following is a little clean up because of the way the CSV file is written
                if len(line[ing]) > 2:
                    if ing != 5: 
                        line[ing] = line[ing][1:] 
                    new_recipe.addIngredient(line[ing])
            recipes.append(new_recipe) # add recipe to list of recipes
    return recipes

