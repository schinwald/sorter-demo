# Description:
# Common functions needed by sorting algorithms
# 
# Author: James Schinwald

# swaps to elements in an array
def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp