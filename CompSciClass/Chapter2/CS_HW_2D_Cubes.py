# CS_HW_2D_Cubes
# Your Name

print("Perfect cubes")

cubes = []
x = 1
while x < 51:
    lolxd = x**3
    cubes.append(lolxd)
    x += 1
x = 0
while x < 50:
    print(str(x + 1) + " cubed is " + str(cubes[x]))
    x += 1
