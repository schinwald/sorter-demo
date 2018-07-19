# Description:
# 
# 
# Author: James Schinwald

def sort(array):
    for i in range(1, len(array)):
        num = array[i]

        j = i-1
        while j >= 0 and num < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = num

def explain():
    print("\n   Insertion Sort:\n")
    # print("      1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).")
    # print("      2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.\n")