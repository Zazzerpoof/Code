import time
import random

def TyperText(line):
    line = list(line)
    x = len(line)
    counter = 0
    print("\n\n\n\n")
    while counter < x:
        print(line[counter], end = "")
        counter += 1
        delaytime = random.randint(1,500)
        delaytime /= 1000
        time.sleep(delaytime)



x = input("Write your story here.\n")

TyperText(x)

