# Description:
# 
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
    pass