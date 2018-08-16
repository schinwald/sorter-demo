# Description:
# Using a nested loop, this selects each element in the array and loops through all elements to the right, finding the smallest number and replacing it with the 
# selected element.
# 
# Author: James Schinwald

from utility import swap

# sorts the array
def sort(array):
    # select an index
    for i in range(0, len(array)):
        lowest = i

        # loop through all elements to the right of the selected index
        # finding the smallest number
        for k in range(i+1, len(array)):
            if array[k] < array[lowest]:
                lowest = k

        # swap smallest number with selected indexed number
        swap(array, i, lowest)

# explanation of the sorting algorithm used
def explain():
    print("\n   Selection Sort:\n")
    print("      Using a nested loop, this selects each element in the array and loops through all elements to the right, finding the smallest number and replacing it with the")
    print("      selected element.\n")
    print("         Steps:\n")
    print("            1. Select the first index in the array and mark it as the smallest number.")
    print("            2. Loop through the rest of the array and select the index of the smallest number, replacing all previous smallest numbers.")
    print("            3. Swap the selected index with the index of the smallest number.")
    print("            4. Increment the selected index by one and repeat steps 2-3 until selected index is equal to the last index of the array.\n")
