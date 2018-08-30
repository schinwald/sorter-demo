# Description:
# Sorts the list relative to each digit using a counting sort algorithm.
# 
# Author: James Schinwald

import math

# sorts the array
def sort(array):
    maximum = max(array)
    exp = 1

    # cycle through each digit and sort relative to that digit
    while math.floor(maximum/exp) > 0:
        sortDigits(array, exp)
        exp *= 10

# sorts each digit using counting sort
def sortDigits(array, exp):
    count = [0 for i in range(0, 10)]
    output = [0 for i in range(0, len(array))]

    # count the number of time a number appears in a specific digit
    for i in range(0, len(array)):
        index = math.floor(array[i] / exp) % 10
        count[index] += 1

    # adjust the count list to index the correct position relative to its previous position
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # store the value indexed by the original list into its correct position using the count list
    for i in range(len(output)-1, -1, -1):
        index = math.floor(array[i] / exp) % 10
        count[index] -= 1
        output[count[index]] = array[i]

    # transfer each value from output back into the original list
    for i in range(0, len(array)):
        array[i] = output[i]

# explanation of the sorting algorithm used
def explain():
    print("\n   Radix Sort:\n")
    print("      Sorts the list relative to each digit using a counting sort algorithm.\n")
    print("         Steps:\n")
    print("            1. Specify the digit in the ones column.")
    print("            2. Create a counting list of size 10 to count each number in the specified digit.")
    print("            3. Adjust the counting list by adding each element by its previous element.")
    print("            4. Loop through each element in the original list to index the sorted position in the counting list and move the element respectively.")
    print("            5. Specify the next digit if applicable and repeat steps 2-5 until there are no more digits left.\n")