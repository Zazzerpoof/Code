# CS_HW_2I_Palindrome
# Gideon Rediger
print("Palindrome Tester")
raw_input = input("Type a word: ")
word = raw_input.lower().strip()
wordlist = list(word)
x=0
real = True
for t in range(0,len(word)//2):
    if wordlist[0 + x] != wordlist[len(word) - x - 1]:
        real = False
    x += 1   
print("Palindrome: " + str(real))


