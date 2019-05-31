# CS_HW_3A_Circle_Analyzer
# Gideon Rediger
print("Circle Analyzer")
import math
def analize_circle(r):
    print("\nCircle Info:\nradius = " + r + "\ndiameter = " + str(2*float(r)) + "\ncircumference = " + str(math.pi * 2 * float(r)) + "\narea = " + str(math.pi * float(r) **2))
r = input("Radius?  ")
analize_circle(r)