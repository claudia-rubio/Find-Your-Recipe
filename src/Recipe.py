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
        print(self.searchFactor)
    def ing_info(self):
        value ="|   "
        #value =  str(self.name) + "   Time:  " + str(self.minutes) + "   Calories:  " + str(self.calories) + "  Steps:   " + str(self.n_s) + "  Ingredients:   "
        for i in self.ingredients:
            value += str(i) + "   |   "
        return value

    #calculate recipe search factor
    #this function determines the value of the member variable that will be used in sorting
    #the values are divided by those number to normaliza the data as much as posible, ex a change of 1 min shouldn't be considered as influential as a change of 1 ingredient
    def calculate_search_factor(self):
        self.searchFactor = 0
        if self.ni_input != False:
            self.searchFactor += abs(self.n_i - self.ni_input)/50
        if self.calories_input != False:
            self.searchFactor += abs(self.calories - self.calories_input)/1000
        if self.time_input != False:
            self.searchFactor += abs(self.minutes - self.time_input)/300
        if self.difficulty_input != False:
            self.searchFactor += abs(self.n_s - self.difficulty_input)/50
    
