# CS_HW_3D_Right_Triangles
# Gideon Rediger
l1 = float(input("Enter three lengths\nLength 1: "))
l2 = float(input("Length 2: "))
l3 = float(input("Length 3: "))
a=0
b=0
c=0
def is_right(l1,l2,l3):    
    if l1 > l2 and l1 > l3:
        c=l1
        b=l2
        a=l3
    elif l2 > l1 and l2 > l3:
        c=l2
        b=l1
        a=l3
    else:
        c=l3
        b=l2
        a=l1 
    if a**2 + b**2 == c**2:
        print("Right Triangle")
    else:
        print("Not Right")
# no pun intended lol
is_right(l1,l2,l3)