# Description:
# Increments through each element in a list (except for the first one) 
# and inserts it into the correct location sequentially using all previous elements
# 
# Author: James Schinwald

def sort(array):
    # select element in array
    for i in range(1, len(array)):
        num = array[i]

        # find the correct spot to put the element and make room
        j = i-1
        while j >= 0 and num < array[j]:
            array[j+1] = array[j]
            j -= 1

        # place element
        array[j+1] = num

def explain():
    print("\n   Insertion Sort:\n")
    print("      Increments through each element in a list (except for the first one) and inserts it into the correct location sequentially using all previous elements.\n")
    print("         Steps:\n")
    print("            1. Start at the 2nd element (Let's refer to it as the \"indexed value\").")
    print("            2. Loop through previous elements until \"indexed value\" is greater than a previous element. During each iteration it should shift the previous element to the right.")
    print("            3. Insert the \"indexed value\" into the correct location using the last known index of the loop.")
    print("            4. Increment to the next \"indexed value\" and repeat steps 2-4 until no more elements remain.\n")