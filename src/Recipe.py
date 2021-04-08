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
    def recipe_info(self):
        value =  str(self.name) + "   Time:  " + str(self.minutes) + "   Calories:  " + str(self.calories) + "  Steps:   " + str(self.n_s) + "  Ingredients:   "
        for i in self.ingredients:
            value += str(i) + ",   "
        return value
        

    #set static variables for comparison, these are set by user input
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
    #this function determines the value of the member variable that will be used in sorting
    def calculate_search_factor(self):
        if self.calories_input != False:
            self.searchFactor += abs(self.calories - self.calories_input)/700
        if self.ni_input != False:
            self.searchFactor += abs(self.n_i - self.ni_input)/9
        if self.time_input != False:
            self.searchFactor += abs(self.minutes - self.time_input)/120
        if self.difficulty_input != False:
            self.searchFactor += abs(self.n_s - self.difficulty_input)/9
    
