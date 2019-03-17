import time
import random

def TyperText(line,speeed):
    line = list(line)
    x = len(line)
    counter = 0
    print("\n\n\n\n")
    while counter < x:
        print(line[counter], end = "")
        counter += 1
        if speeed == "s": 
            delaytime = random.randint(1,500)
            delaytime /= 1000
        elif speeed == "m":
            delaytime = random.randint(1,250)
            delaytime /= 1000
        elif speeed == "f":
            delaytime = random.randint(1,100)
            delaytime /= 1000
        elif speeed == "v":
            delaytime = random.randint(1,50)
            delaytime /= 1000
        time.sleep(delaytime)



x = input("Write your story here.\n")

speed = input("How fast do you want the text? slow (s), medium (m), fast (f), or very fast (v)?")
while speed != "s" and speed != "m" and speed != "f" and speed != "v":
    speed = input("No U MORON!\nHow fast do you want the text? slow (s), medium (m), fast (f), or very fast (v)?\n")


TyperText(x,speed)

# suggested story: Once upon a time a farty nerd tooted on the queen of England. "YOU FRIKKING MORON!" she screamed at him, "I HATE YOU! DIE!" and she shot a bolt of lightning from her hand. The shimmering, cracklingg beam of pure energy shot from her hand like an arrow from a bow, phasing through the air at incredible speeds. With a huge explosion, it struck the fart nerd directly in the chest. A large boom fillec the hall as a bout of flame and pressure exploded form the nerd, blood and gore splattering everything but the queen. "Rekt." she tossed offhandedly of her shoulder asshe smugly exited the room.