from Recipe import Recipe
import csv

class Recipes:
    recipes = []

    def __init__(self):
        #reads the information from the CSV file
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
                self.recipes.append(new_recipe) # add recipe to list of recipes
        

    def search_ingredient(self, target):
        output = []
        for i in self.recipes:
            for j in i.ingredients:
                if target in j:
                    output.append(i)
        self.recipes = output







        

   