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
    
    #heapify for sorting
    def heapify(self, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        self.recipes[largest].calculate_search_factor()     

        if l < n:
            self.recipes[l].calculate_search_factor()
            if self.recipes[largest].searchFactor < self.recipes[l].searchFactor:
                largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n:
            self.recipes[r].calculate_search_factor()
            if self.recipes[largest].searchFactor < self.recipes[r].searchFactor:
                largest = r
    
        # Change root, if needed
        if largest != i:
            self.recipes[i], self.recipes[largest] = self.recipes[largest], self.recipes[i]  # swap
            # Heapify the root.
            self.heapify(n, largest)
 
    #heap sort
    def heapSort(self):
        n = len(self.recipes)

        # Build a maxheap.
        for i in range(n//2 - 1, -1, -1):
            self.heapify(n, i)
        # One by one extract elements
        for i in range(n-1, 0, -1):
            self.recipes[i], self.recipes[0] = self.recipes[0], self.recipes[i]  # swap
            self.heapify(i, 0)


# implementation of MergeSort
def mergeSort(recipes):
    if len(recipes) > 1:

        # Finding the mid of the array
        mid = len(recipes)//2

        # Dividing the array elements
        L = recipes[:mid]

        # into 2 halves
        R = recipes[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            L[i].calculate_search_factor()
            R[i].calculate_search_factor()
            if L[i].searchFactor < R[j].searchFactor:
                recipes[k] = L[i]
                i += 1
            else:
                recipes[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            recipes[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            recipes[k] = R[j]
            j += 1
            k += 1









        

   