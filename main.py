 # Description:
# 
# 
# Author: James Schinwald

import os
import time
import random

import sorter

def randomList(size):
    array = []

    for i in range(1, size):
        array.insert(random.randint(0, i-1), i)

    return array

def algToString(alg):
    string = ""

    for i, v in enumerate(alg):

        valg = "".join([str(i+1), ". ", v]) 

        if i % 3 == 0:
            string = "".join([string, f"   |  {valg:^19}"])
        elif i % 3 == 1:
            string = "".join([string, f"{valg:^19}"])
        elif i % 3 == 2:
            string = "".join([string, f"{valg:^19}  |"])
            if i != len(alg) - 1:
                string = "".join([string, "\n"])

    leftOver = -(i % 3) + 2
    if leftOver != 0:
        string = "".join([string, leftOver * " " * 19, "  |"])

    return string

def createTable(salg):
    print("\n   +-------------------------------------------------------------+")
    print("   |  Welcome to my demonstration of various sorting algorithms  |")
    print("   +-------------------------------------------------------------+")
    print(salg)
    print("   +-------------------------------------------------------------+\n")

alg = ("Merge Sort", "Bubble Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort")
falg = ("Merge Sort", "Bubble Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort", "Quick Sort")
salg = algToString(alg)
array = randomList(10)

os.system('cls')

# t = 0
# merge.explain()
# while t <= 3:
#     createTable(salg)
#     print("   Generating random list", t * ".")
#     time.sleep(1)
#     t += 1
#     os.system('cls')

createTable(salg)
print("   Randomly generated list: ", array, "\n")

time.sleep(1)
print("   Which algorithm would you like to use?")

sel = input("                        Algorithm number: ")
while int(sel) not in range(1, len(alg)):
    os.system('cls')
    createTable(salg)
    print("   Randomly generated list: ", array, "\n")
    print("   Which algorithm would you like to use? Invalid number!")
    sel = input("                        Algorithm number: ")

os.system('cls')

sort.merge.explain()
print("\n   ", alg[int(sel)-1], ":")
print("      ...description...")