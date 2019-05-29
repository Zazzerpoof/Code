# CS_HW_2H_Three_Doubles.py
# Gideon Rediger
# Open the file
f = open(r"C:\Users\gidre\Desktop\Code\words.txt")
triplewords = []
total = 0
for line in f:
    word = line.strip()
    rawword = word
    word = list(word)
    x=0
    minitotal = 0
    for cntr in range(0,len(word)-1):
        if word[len(word)-1-x] == word[len(word)-2-x]:
            minitotal += 1
        x+=1
    if minitotal >= 3:
        total += 1
        triplewords.append(rawword)
t=0
for lol in triplewords:
    print(triplewords[t])
    t+=1

print("Total Number: " + str(total))