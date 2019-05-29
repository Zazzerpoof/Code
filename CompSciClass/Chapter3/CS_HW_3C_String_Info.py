# CS_HW_3C_String_Info
# Gideon Rediger
print("String Info")
s = input("Type a word or phrase: ")
def string_info(s):
    c=0
    w=1
    d=0
    l=0
    s = list(s)
    for letter in s:
        c+=1
        if letter == " ":
            w+=1
        elif letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9" or letter == "0":
            d+=1
        elif letter == "a" or letter == "b" or letter == "c" or letter == "d" or letter == "e" or letter == "f" or letter == "g" or letter == "h" or letter == "i" or letter == "j" or letter == "k" or letter == "l" or letter == "m" or letter == "n" or letter == "o" or letter == "p" or letter == "q" or letter == "r" or letter == "s" or letter == "t" or letter == "u" or letter == "v" or letter == "w" or letter == "x" or letter == "y" or letter == "z":
            l+=1
        else:
            pass
    print("\nString Info:\ncharacters: " + str(c) + "\nwords: " + str(w) + "\ndigits: " + str(d) + "\nletters: " + str(l))
string_info(s)