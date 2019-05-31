import math
import random
import datetime
from datetime import date
#The first function is an input validator
def input_validation(description,input_out_of_range,max,min):
    counter = 0
    c = False
    while c == False:
        if counter == 0:
            i = input(description)
        while len(i) == 0:
            i = input("Error: No input. Please input something: ")
        g = True
        if int(i) > max or int(i) < min:
            g = False
        if g == True:
            c = True
        else:
            i = input(input_out_of_range)
        counter += 1
    return i

def square_root():
    i = input_validation("This function prints a square root. Enter a number (1 - 9999): ", "Error: Number out of system range. Please input a valid number: ", 9999, 1)
    print("\nThe square root of " + i + " is " + str(math.sqrt(int(i))))

def test_score():
    c = False
    counter = 0
    #The following loop is an input validator; i didnt use the function because this one is slightly different
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

def taxes():
    i = input_validation("This funtion shows how much your sales tax (7.5%) is for your purchase. Enter the purchase amount (<10,000): ", "Error: input out of range. Please input a valid number: ", 9999, 0)
    print("The sales tax on $" + i + " is $" + str(float(i) * 0.075) + " and the total cost is $" + str(float(i) + float(i) * 0.075))

def randomness():
    print("The random number between 1 and 100 is " + str(random.randint(1,100)))

def daydif():
    counter = 0
    c = False
    while c == False:
        p = False
        if counter == 0:
            i = input("This function shows how many days there are between today and a date you enter. Enter the date in this format (mm/dd/yy): ")
        i = i.split("/")
        while len(i) != 3:
            i = input("Error: invalid string. Please enter something in the format provided: ")
            i = i.split("/")
        g = True
        for x in range(0,3):

            if x == 1:
                if int(i[0]) > 12 or int(i[0]) < 1:
                    g = False
            elif x == 2:
                if int(i[1]) > 31 or int(i[0]) < 1:
                    g = False 
            else:
                if int(i[2]) > 9999 or int(i[2]) < 1:
                    g = False
        if g == True:
            c = True
        else:
            i = input("Error: One or more numbers out of system range. Please input only valid numbers: ")
        counter += 1
    d1 = date(int(i[2]),int(i[0]),int(i[1]))
    if d1 > date.today():
        print("The number of days between " + str(d1) + " and today is " + str(d1 - date.today())) 
    else:
        print("The number of days between " + str(d1) + " and today is " + str(date.today() - d1)) 
daydif()
