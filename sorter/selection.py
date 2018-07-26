 # Description:
# Using a nested loop, this selects each element in the array and loops through all elements to the right, finding the smallest number and replacing it with the 
# selected element.
# 
# Author: James Schinwald

# sorts array using selection sort algorithm
def sort(array):
    # selects each element in the array
    for i in range(0, len(array)):
        lowest = i

        # loops through all elements to the right of selection find the lowest number
        for k in range(i+1, len(array)):
            if array[k] < array[lowest]:
                lowest = k

        # places the lowest number in selected position
        swap(array, i, lowest)

# swaps elements in an array
def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

# explanation of algorithm
def explain():
    print("\n   Selection Sort:\n")
    print("      Using a nested loop, this selects each element in the array and loops through all elements to the right, finding the smallest number and replacing it with the 
    print("      selected element.\n")
    print("         Steps:\n")
    print("            1. Select the first index in the array and mark it as the smallest number.")
    print("            2. Loop through the rest of the array and select the index of the smallest number, replacing all previous smallest numbers.")
    print("            3. Swap the selected index with the index of the smallest number.")
    print("            4. Increment the selected index by one and repeat steps 2-3 until selected index is equal to the last index of the array.")