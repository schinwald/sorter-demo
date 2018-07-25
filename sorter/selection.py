 # Description:
# 
# 
# Author: James Schinwald

def sort(array):
    for i in range(0, len(array)):
        lowest = i

        for k in range(i+1, len(array)):
            if array[k] < array[lowest]:
                lowest = k

        swap(array, i, lowest)

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def explain():
    pass