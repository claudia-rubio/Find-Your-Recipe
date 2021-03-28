'''from Recipe import Recipe
import csv

#reading the information from the CSV file
def readData():
    recipes = []
    with open('dataset/recipes.CSV', newline='') as f:
        file = csv.reader(f)
        
        for line in file:
            #create new recipe
            new_recipe = Recipe(line[0], line[1], line[2], line[3], line[4])
            #add its ingredients
            for ing in range(5, len(line)):
                #the following is a little clean up because of the way the CSV file is written
                if len(line[ing]) > 2:
                    if ing != 5: 
                        line[ing] = line[ing][1:] 
                    new_recipe.addIngredient(line[ing])
            recipes.append(new_recipe) # add recipe to list of recipes
    return recipes
'''






        

   