# Description:
# This sorting algorithm uses max heaps to find the largest value in an array and then isolates said value
# By recursively doing this, each isolated value forms a new array, which has been fully sorted
# 
# Author: James Schinwald

def sort(array):
    # build a max heap
    for i in range((int)(len(array) / 2) - 1, -1, -1):
        heapify(array, len(array), i)

    # swap each
    for size in range(len(array), 0, -1):
        swap(array, 0, size-1)

        # Only one iteration is needed per swap because most of the heap is a max heap
        heapify(array, size-1, 0)

def heapify(array, size, i):
    highest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # checks if left child is higher than parent
    if left < size:
        if array[highest] < array[left]:
            highest = left
    
    # checks if right child is higher than parent
    if right < size:
        if array[highest] < array[right]:
            highest = right

    # if swapped, recursively go through children to adjust for changes
    if highest != i:
        swap(array, highest, i)
        heapify(array, size, highest)

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def explain():
    print("\n   Heap Sort:\n")
    print("      1. Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.")
    print("      2. Swap the first element of the list with the final element. Decrease the considered range of the list by one.")
    print("      3. Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.")
    print("      4. Go to step (2) unless the considered range of the list is one element.\n")