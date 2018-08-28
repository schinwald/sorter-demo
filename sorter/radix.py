# Description:
# 
# Author: James Schinwald

import math

# sorts the array
def sort(array):
    maximum = max(array)
    exp = 1

    while math.floor(maximum/exp) > 0:
        sortDigits(array, exp)
        exp *= 10

# sorts each digit using counting sort
def sortDigits(array, exp):
    count = [0 for i in range(0, 10)]
    output = [0 for i in range(0, len(array))]

    for i in range(0, len(array)):
        index = math.floor(array[i] / exp) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(output)-1, -1, -1):
        index = math.floor(array[i] / exp) % 10
        count[index] -= 1
        output[count[index]] = array[i]

    for i in range(0, len(array)):
        array[i] = output[i]

# explanation of the sorting algorithm used
def explain():
    pass