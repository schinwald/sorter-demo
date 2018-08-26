# Description:
# 
# Author: James Schinwald

# sorts the array
def sort(array):
    count = []
    output = [0 for i in range(len(array))]

    for i in range(0, len(array)):
        index = array[i]

        while index >= len(count):
            count.append(0)

        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(0, len(array)):
        index = count[array[i]]-1
        count[array[i]] -= 1
        output[index] = array[i]

    for i in range(0, len(array)):
        array[i] = output[i]

# explanation of the sorting algorithm used
def explain():
    pass