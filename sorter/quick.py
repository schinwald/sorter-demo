# Description:
# Partitions the array in 3 sections, one for the pivot, one for all the numbers smaller than the pivot, and one for all the numbers larger than the pivot.
# Organizes the partitions in ascending order (ie. smallest, pivot, largest) and then recursively partitioning and organizing the smaller and larger sides until 
# everything is fully sorted.
# 
# Author: James Schinwald

def sort(array):
    partitioner(array, 0, len(array)-1)

def partitioner(array, low, high):
    mid = partition(array, low, high)

    if mid != low:
        partitioner(array, low, mid-1)

    if mid != high:
        partitioner(array, mid+1, high)

def partition(array, low, high):
    pivot = array[high]
    
    j = low
    for i in range(low, high+1):
        if array[i] <= pivot:
            swap(array, i, j)
            j += 1

    return j-1
        
def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def explain():
    print("\n   Quick Sort:\n")
    print("      Partitions the array in 3 sections, one for the pivot, one for all the numbers smaller than the pivot, and one for all the numbers larger than the pivot.")
    print("      Organizes the partitions in ascending order (ie. smallest, pivot, largest) and then recursively partitioning and organizing the smaller and larger sides until") 
    print("      everything is fully sorted.\n")
    print("         Steps:\n")
    print("            1. Declare the last index as the pivot point.")
    print("            2. Loop through the specified section of the array shifting all numbers smaller than the pivot to the left; subsequently, leaving all larger numbers on the right.")
    print("            3. Change specified section of array to be the smaller half and repeat step 2. using recursion until there is nothing left.")
    print("            3. Change specified section of array to be the larger half and repeat step 2. using recursion until there is nothing left.\n")