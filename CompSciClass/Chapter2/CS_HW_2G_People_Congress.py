# CS_HW_2G_People_Congress
# Gideon Rediger

# Open the file
#Note to whoever is grading this: I had to change the path name because of the IDE I am using. It might need to be changed before the assignment is graded.
f = open(r"C:\Users\gidre\Desktop\Code\usaconst.txt")

# Count the number of times "people" appears
# and the number of times "congress" appears
p = 0
c = 0
for line in f:
    x = line.strip().lower()
    x = x.split()
    o=0
    for t in x:
        if "congress" in x[o]:
            c += 1
        
        elif "people" in x[o]:
            p += 1
        else:
            pass
        o+=1
print("People: " + str(p) + "\nCongress: " + str(c))
