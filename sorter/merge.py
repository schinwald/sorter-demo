# Merge Sort
# 
# Description:
# 
# 
# Author: James Schinwald

import numpy

# creates
def sort(array):
    if len(array) > 1:
        # split the arrays
        combined = []
        middle = (int)((len(array) + 1) / 2)
        split = numpy.split(array, [middle, len(array)])

        aSplit = sort(split[0])
        bSplit = sort(split[1])
        
        i = 0
        j = 0
        # sort and combine each of the arrays
        while i < len(aSplit) and j < len(bSplit):
            if aSplit[i] < bSplit[j]:
                combined.append(aSplit[i])
                i += 1
            elif bSplit[j] < aSplit[i]:
                combined.append(bSplit[j])
                j += 1
            else:
                combined.append(aSplit[i])
                combined.append(bSplit[j])
                i += 1
                j += 1

        # append the rest of the array
        if i < len(aSplit):
            for x in range(i, len(aSplit)):
                combined.append(aSplit[x])
        elif j < len(bSplit):
            for x in range(j, len(bSplit)):
                combined.append(bSplit[x])
        
        return combined
    else:
        return array

def explain():
    print("\n   Merge Sort:\n")
    print("      1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).")
    print("      2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.\n")