import math
import random
import time
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
    i = input_validation("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis function prints a square root. Enter a number (1 - 9999): ", "Error: Number out of system range. Please input a valid number: ", 9999, 1)
    print("\n\n\nThe square root of " + i + " is " + str(math.sqrt(int(i))))

def test_score():
    c = False
    counter = 0
    #The following loop is an input validator; i didnt use the function because this one is slightly different
    while c == False:
        if counter == 0:
            i = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter any number of test scores (1 - 100). Seperate each by a space: ")
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
    print("\n\n\nThe test average is " + str(t) + "%")

def taxes():
    i = input_validation("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis funtion shows how much your sales tax (7.5%) is for your purchase. Enter the purchase amount (<10,000): ", "Error: input out of range. Please input a valid number: ", 9999, 0)
    print("The sales tax on $" + i + " is $" + str(float(i) * 0.075) + " and the total cost is $" + str(float(i) + float(i) * 0.075))

def randomness():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe random number between 1 and 100 is " + str(random.randint(1,100)))

def daydif():
    counter = 0
    c = False
    while c == False:
        p = False
        if counter == 0:
            i = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis function shows how many days there are between today and a date you enter. Enter the date in this format (mm/dd/yy): ")
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
        print("\n\n\nThe number of days between " + str(d1) + " and today is " + str(d1 - date.today())) 
    else:
        print("\n\n\nThe number of days between " + str(d1) + " and today is " + str(date.today() - d1)) 
stop = False
trustop = False
x = time.time()
while trustop == False:
    while stop == False:

        i = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMy Custom Functions\n1. What's the root?\n2. Average my test scores.\n3. Show me the tax.\n4. Randomness.\n5. How many days?\n6. Exit\n Enter an option: ")
        while i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6":
            i = input("Error: invalid input. Please enter a valid command: ")
        if i == "1":
            square_root()
            input("Press Enter to continue")
        elif i == "2":
            test_score()
            input("Press Enter to continue")
        elif i == "3":
            taxes()
            input("Press Enter to continue")
        elif i == "4":
            randomness()
            input("Press Enter to continue")
        elif i == "5":
            daydif()
            input("Press Enter to continue")
        else:
            stop = True
    i = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAre you sure you want to quit? (y or n)\n")
    while i != "y" and i != "n":
        i = input("Error: Please enter a valid command. \nAre you sure you want to quit? (y or n)\n")
    if i == "y":
        trustop = True
    else:
        stop = False
y = round(time.time() - x)
seconds = str(y % 60)
minutes = str(y // 60)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThank you. You used the system for " + minutes + " minutes and " + seconds + " seconds. You will be charged $" + str(y * 0.25) + ".")

