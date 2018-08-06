# Description:
# 
# Author: James Schinwald

# sorts the array
def sort(array):
    for i in range(len(array)-1, 0, -1):
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
    pass