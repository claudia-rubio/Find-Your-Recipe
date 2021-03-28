class Recipe:
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
        print("Name:      " + self.name)
        print("Minutes:   " + self.minutes)
        print("Calories:  " + self.calories)
        print("Ingredients  (" + self.n_i + ") :")
        for item in self.ingredients:
            print("\t-" + item)