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
        
    #this function returns a list of recipes that only contain the searched ingredient
    def search_ingredient(self, target):
        output = []
        for i in self.recipes:
            for j in i.ingredients:
                if target in j:
                    output.append(i)
        if len(output) > 0 :
            self.recipes = output


    #partition for quick sort
    def partition(self, low, high):
        i = (low-1)         # index of smaller element
        self.recipes[high].calculate_search_factor()
        
        pivot = self.recipes[high].searchFactor     # pivot
    
        for j in range(low, high):
            self.recipes[j].calculate_search_factor()
            if self.recipes[j].searchFactor <= pivot:
                # increment index of smaller element
                i = i+1
                self.recipes[i], self.recipes[j] = self.recipes[j], self.recipes[i]
    
        self.recipes[i+1], self.recipes[high] = self.recipes[high], self.recipes[i+1]
        return (i+1)
    
    #quick sort
    def quickSort(self, low, high):
        if len(self.recipes) == 1:
            return
        if low < high:
    
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(low, high)
    
            # Separately sort elements before
            # partition and after partition
            self.quickSort(low, pi-1)
            self.quickSort(pi+1, high)
  
    #todo other sorting method







        

   