# Description:
# Creates a list that stores the frequency of each value and adjusts the frequency by adding it by its previous element. This gives you the sorted position of
# each element in the original list. Then, it iterates through the original list, moving all elements to its appropriate location.
# 
# Author: James Schinwald

# sorts the array
def sort(array):
    count = []
    output = [0 for i in range(len(array))]

    # count the number of times each value is in the list
    for i in range(0, len(array)):
        index = array[i]

        while index >= len(count):
            count.append(0)

        count[index] += 1

    # adjust the count list to index the correct position relative to its previous position
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # store the value indexed by the original list into its correct position using the count list
    for i in range(0, len(array)):
        index = count[array[i]]-1
        count[array[i]] -= 1
        output[index] = array[i]

    # transfer each value from output back into the original list
    for i in range(0, len(array)):
        array[i] = output[i]

# explanation of the sorting algorithm used
def explain():
    print("\n   Counting Sort:\n")
    print("      Creates a list that stores the frequency of each value and adjusts the frequency by adding it by its previous element. This gives you the sorted position of")
    print("      each element in the original list. Then, it iterates through the original list, moving all elements to its appropriate location.\n")
    print("         Steps:\n")
    print("            1. Create a counting list that stores the number of times a value is in the original list.")
    print("            2. Adjust the counting list by adding each element by its previous element.")
    print("            3. Loop through each element in the original list to index the sorted position in the counting list and move the element respectively.\n")