# Description:
# 
# 
# Author: James Schinwald

import numpy

def sort(array):
    if len(array) > 1:
        # split the arrays
        middle = (int)((len(array) + 1) / 2)
        split = numpy.split(array, [middle, len(array)])

        array_a = split[0].tolist()
        array_b = split[1].tolist()

        sort(array_a)
        sort(array_b)

        i = 0
        j = 0
        k = 0
        # sort and combine each of the arrays
        while i < len(array_a) and j < len(array_b):
            if array_a[i] < array_b[j]:
                array[k] = array_a[i]
                i += 1
            elif array_b[j] < array_a[i]:
                array[k] = array_b[j]
                j += 1
            else:
                array[k] = array_a[i]
                array[k] = array_b[j]
                i += 1
                j += 1

            k += 1

        # append the rest of the array
        if i < len(array_a):
            for x in range(i, len(array_a)):
                array[k+x-i] = array_a[x]
        elif j < len(array_b):
            for x in range(j, len(array_b)):
                array[k+x-j] = array_b[x]

def explain():
    print("\n   Merge Sort:\n")
    print("      1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).")
    print("      2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.\n")