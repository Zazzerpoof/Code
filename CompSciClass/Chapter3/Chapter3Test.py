import math
import random
import time

def square_root():
    counter = 0
    c = False
    #The following loop is an input validator
    while c == False:
        if counter == 0:
            i = input("This function prints a square root. Enter a number (1 - 9999): ")
        while len(i) == 0:
            i = input("Error: No input. Please input something: ")
        g = True
        if int(i) > 9999 or int(i) < 1):
            g = False
        if g == True:
            c = True
        else:
            i = input("Error: Number out of system range. Please input a valid number: ")
    #This is the actual program
    print("\nThe square root of " + i + " is " + str(math.sqrt(int(i))))

def test_score():
    c = False
    counter = 0
    #The following loop is an input validator
    while c == False:
        if counter == 0:
            i = input("Enter any number of test scores (1 - 100). Seperate each by a space: ")
        while len(i) == 0:
            i = input("Error: No input. Please input something: ")
        i = i.split()
        g = True
        for x in i:
            if int(x) > 100 or int(x) < 1:
                g = False
        if g == True:
            c = True
        else:
            i = input("Error: One or more numbers out of system range. Please input only valid numbers: ")
        counter += 1
            

    #This is the actual function
    t = 0
    for x in i:
        t += int(x)
    t /= len(i)
    print("\nThe test average is " + str(t) + "%")
test_score()