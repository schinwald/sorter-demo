# Description:
# 
# Author: James Schinwald

import numpy

RUN = 32

# sorts the array
def sort(array):
    if len(array) > RUN:
        split = numpy.split(array, [RUN, len(array)])

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
                array[k+1] = array_b[j]
                i += 1
                j += 1
                k += 1

            k += 1

        # append the rest of the array
        if i < len(array_a):
            for x in range(i, len(array_a)):
                array[k+x-i] = array_a[x]
        elif j < len(array_b):
            for x in range(j, len(array_b)):
                array[k+x-j] = array_b[x]
    else:
        for i in range(1, len(array)):
            num = array[i]

            # find the correct spot to put the element and make room
            j = i-1
            while j >= 0 and num < array[j]:
                array[j+1] = array[j]
                j -= 1

            # place element
            array[j+1] = num

# explanation of the sorting algorithm used
def explain():
    pass