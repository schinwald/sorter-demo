# Description:
# Swaps adjacent elements until greater elements are shifted to the end of a specified range. Repeating these steps while reducing the range of the array to be 
# sorted.
# 
# Author: James Schinwald

# sorts the array
def sort(array):
    # specifies the range to be sorted
    for i in range(len(array)-1, 0, -1):
        # swaps all adjacent elements that are greater
        for j in range(0, i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                
# swaps to elements in an array
def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

# explanation of the sorting algorithm used
def explain():
    print("\n   Bubble Sort:\n")
    print("      Swaps adjacent elements until greater elements are shifted to the end of a specified range. Repeating these steps while reducing the range of the array to be")
    print("      sorted.\n")
    print("         Steps:\n")
    print("            1. Specify a range spanning the entire array.")
    print("            2. Loop through elements in a specified range, swapping with adjacent elements to the right when larger.")
    print("            3. Reduce the maximum in the specified range by one and repeat steps 2-3 until the min is equal to the max in the range.\n")