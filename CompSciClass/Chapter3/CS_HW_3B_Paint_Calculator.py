# CS_HW_3B_Paint_Calculator
# Gideon Rediger
print("Paint Calculator")
import math
w = input("Width in feet?  ")
h = input("Hight in feet?  ")
def calculate_paint(w,h):
    print("\nArea = " + str(float(w) * float(h)) + "\n" + str(math.ceil((float(w) * float(h)) / 350)) + " gallons of paint required")
calculate_paint(w,h)    