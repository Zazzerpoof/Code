# CS_HW_2F_Twenty_Letters
# Gideon Rediger

# Open the file
#Note to whoever is grading this: I had to change the path name because of the IDE I am using. It might need to be changed before the assignment is graded.
f = open(r"C:\Users\gidre\Desktop\Code\words.txt")
longwords = 0
longwordslist = []
for line in f:
    word = line.strip()
    if len(word) >= 20:
        longwords += 1
        longwordslist.append(word)
x=0
for t in longwordslist:
    print(longwordslist[x])
    x+=1
print("Total Number: " + str(longwords))
