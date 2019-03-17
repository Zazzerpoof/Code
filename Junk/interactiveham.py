
#Functions

def checkdead(lives,score):
    if lives == 0:
        print("Wow u fail loser.")
        print("\nYour Score: " + str(score))
        exit()





#Basic Variables

Correct = 0
Lives = 100
holdingsword = "no"




#Intro

input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Hi, time to test u with random stuff! When I ask a yes or no question, please respond with y or n.\n")
q1 = input("Cool! \nFirst I'll check on your Hamilton skillz. I'll say the first line and you reply with no caps or punctuation.\nSound good? \n")
if q1 == "y":
    pass
else:
    repeat1 = 0
    print("I JUST GAVE U A FORMAT TO RESPOND IN U MORON!!! READ THE IMSTRUCTIONS DUMMY!!!!!")
    while repeat1 != "y":
        repeat1 = input("\nDO U UNDERSTAND??????\n")

#Question #1

q2 = input("\nAre you ready? \n")
while q2 != "y":
    q2=input("\nNO U MORON!!! ANSWER IN THE RIGHT FORMAT!!!!!!!! \nNow are u ready?\n")


line1 = input("1: I'm John Laurens in the place to be;  (Last Word:Three) \n")
if line1 == "a two pints of sam adams but im working on three":
    print("\nNiiiiice!!!")
    Correct += 1
else:
    print("\nu fail loser \n\n\n")
    Lives -= 1

#Question #2

line2 = input("2: What is the answer to Life, the Universe, and Everything?\n")
if line2 == "42":
    print("\nNice, man!\n\n")
    Correct += 1
else:
    print("\nwow ur a total losing failure.\n")
    Lives -= 1

checkdead(Lives,Correct)

#Question #3

line3 = input("How many logs does it take to craft a door?\n")
if line3 == "1.5" or line3 == "1 1/2":
    print("\nGreat jobbe\n\n")
    Correct += 1
else:
    print("\nwow u realy r thu wuurst\n\n")
    Lives -= 1

checkdead(Lives,Correct)

#Question #4

'''
def rorl(message, errormessage, abrmessage):
    x = input(message)
    while not (x == "r" or x == "l"):
        print(errormessage)
        x = input(abrmessage)
    return x
    

line4 = rorl("You are walking in a hallway. You reach a T intersection. Do you go right (r) or left (l)?\n", \
             "Wow man u reely r thu wurst. I gave u all the dang instructions in the text itself but u just r too stoopid 2 listen dumbo\n", \
             "Do you go right (r) or left (l)?\n")
'''

line4=input("You are walking in a hallway. You reach a T intersection. Do you go right (r) or left (l)?\n")
while not (line4 == "r" or line4 == "l"):
    print("\nWow man u reely r thu wurst. I gave u all the dang instructions in the text itself but u just r too stoopid 2 listen dumbo\n\n")
    line4=input("Do you go right (r) or left (l)?\n")

if line4 == "r":
    print("You turn right and emerge into a large room full of gistening piles of treasure. You walk over mountains of gold coins,\nrich tapesrites, and glistening armor to find a solitary plaque hanging on the wall.\nYou approach and read it. \"Right really was the right way to go\" it says.\"\n Congrats bro you've passed\n\n")
    Correct += 1
else: #(l)

    line4andahalf = input("\nYou turn leftk and travel down the long hallway. When you reach the end, you see two doors on either side of the corridor.\n Do you go into the right door (r) or the left door (l)?\n")
    while not (line4andahalf == "r" or line4andahalf == "l"):
        print("u dumm boi yooz the rite form")
        line4andahalf = input("Do u go right (r) or left (l)?\n")

    if line4andahalf == "r":
        print("\nYou enter the room and hear a muted oily click. You whirl around to see the door slam shut.\n You race over and tug at the latch,but a metal beam pressing against the door prevails over your vain attemts to escape.\n The gravelly sound of moving rock and the whirring of ancient machinery fill the small room. You gasp in horror as you notice that they walls are slowly closing in on you.\nAs they get closer, you futily bang and kick on the door but nothing happens. Finally you are smashed between the gigantic rocks, and nobody but the rats outside can hear your screams.\nYou are Dead.\n\n")
        Lives -= 1

    else: # "l"
        print("\nYou enter the room and hear a rough scraping sound. You whirl around and watch in horror\nas the door you came through is replaced with a large stone slab that completely blocks your escape. There is hole high in the roof overhead where the sun casts a single beam down from the heavens.\nYou futilely try to climb the steep rocky walls but they have been polished so smoothly that you cannot find any hold at all.\nYou sink to the floor in sadness and despair as you realize that there is no escape  and that you will die in this very room.\nYou lean against the smooth wall and stare blankly at the other wall, your spirit shattered.\nSeveral days later you are still in that position, your mind vacant, your body overheated but not sweaty because of your extreme dehydration.\nYour tongue lies thick and swollen in your mouth, and your throat has the consistancy of sand. Your eyeballs have begun to shrivel and sink deep into your bloated but gaunt features.\nFinally, exaustion and sheer dehydration saps the remaining strength from your belabored muscles and your slide down the wall onto your back, your face in the shaft on sunlight.\nThe sunlight begins to glare as your shrunken eyes stare emptily at the walls, the world getting brighter and brighter until everything gradually fades into blackness.\nYou are Dead.\n\n")
        Lives -= 1
    
checkdead(Lives,Correct)

#Question 5

line5 = input("Would you rather play Minecraft or Roblox?\n")
while not(line5 == "minecraft" or line5 == "roblox"):
    print("Just answer the question already.\n")
    line5 = input("MINECRAFT OR ROBLOX?!?!?!?!?\n")

if line5 == "minecraft":
    print("u see sense. Good Job.\n")
    Correct += 1

else:
    print("What the heck is wrong with you?? You're gonna lose more then just one life for this.\n")
    Lives -= 1

checkdead(Lives,Correct)



#Question 6

line6 = input("\n\nType the answer: 675.986+345/62.3*0*9.6-80/-674-764/-85*-8556644654?\n")
if line6 == "0":
    print("dang boi u gud\n")
    Correct += 1

else:
    print("ur wrong u stupid dum hed\n")
    Lives -= 1

checkdead(Lives,Correct)

#Question 7

line7a = input("I say jump.\nDo you jump?\n")
while not(line7a == "y" or line7a == "n"):
    print("JUST DO IT!!!\n")
    line7a = input("Do u jump?\n")

if line7a == "y":
    print("Good!\n")

    line7b = input("I say wave.\nDo you wave?\n")
    while not(line7b == "y" or line7b == "n"):
        print("dumbus write coerektlee\n")
        line7b = input("Do u wave?\n")
    if line7b == "y":
        print("Great!\n")


        line7c = input("Clap.\nDo u clap?\n")
        while not(line7c == "y" or line7c == "n"):
            print("write right, it's a rite.")
            line7c = input("Do u clap?")
        if line7c == "y":
            print("BUT I DIDN'T SAY")
            Lives -= 1

        else:
            print("gud kech bro")
            Correct += 1

    else:
        "oi i said to wave dawg ur loozin a lief\n"
        Lives -= 1

    
else:
    print("oi i said to jump dawg u r losin a lief\n")
    Lives -= 1

checkdead(Lives,Correct)

#Question 8

line8 = input("You are in a small room with two things: a cabinet (c) and a door (d). Where do you go?\n")
while not(line8 == "c" or line8 == "d"):
    print("Input the right thing and stop being difficult.")
    line8 = input("Cabinet (c) or Door (d)?\n")

if line8 == "c":
    line8a = input("You see a sword in the cabinet. Do you pick it up?\n")
    while not(line8a == "y" or line8a == "n"):
        print("Input the right thing and stop being difficult.")
        line8a = input("Do you pick up the sword?")

    if line8a == "y":
        print("Sword equipped.")
        holdingsword = "yes"

    else:
        pass

    line8b = input("Now do you go through the door?")
    while not(line8b == "y"):
        if line8b == "n":
            print("There isn't anything else to do.")
        else:
            print("Input the right thing and stop being difficult.")
        line8b = input("Do you go through the door?")

    if holdingsword == "yes":
        line8c = input("you enter a long corridor. As you round a bend you suddenly encounter a troll! It glares at you and moves incredibly quickly and agressively towards you.\nYou can either run (r), fight with your sword (f), or try to befriend it (b). What do you do?\n")
        while not(line8c == "r" or line8c == "f" or line8c == "b"):
            print("Come on man. Just put in the right thing.")
            line8c = input("do you run (r), fight (f), or befriend (b)?")

        if line8c == "r":
            print("You turn and flee but the troll catches you after only three steps. you feel his enormous fangs sink into you and your lifeblood\nseeps onto the ground. The last thing you hear is the crunching sound of your own bones.\nYou are Dead.\n")
            Lives -= 1

        elif line8c == "f":
            print("You turn to face the charging troll are you swing your sword at it's knee, the highest place you can reach.\nThe swing is so powerful it cuts cleanly through and the troll's thigh slides sideways off of the knee, blood spilling everywhere.\nYou back off as the troll screams in agony. You step back and wait until the troll is weak from bloodloss and then you step forward and stab it right in the eye.\nWith a final moan, the troll rolls over and dies and you go on your merry way.\nCongrats man.")
            Correct += 1

        else:
            print("You turn and try to say something but the troll has shoved you in his mouth before you can even think.\n You die it agony as you are chewed by the blunt, bludgeoning molars of the troll. The last thing you hear is the snapping and crunching of your own bones.\nYou are Dead.")        
            Lives -= 1

    else:
        line8d = input("You enter a long corridor. As you round a bend you suddenly encounter a troll! It glares at you and moves incredibly quickly and agressively towards you.\nYou can either run (r), fight with fists (f), or try to befriend it (b). What do you do?\n")
        
        while not(line8d == "r" or line8d == "f" or line8d == "b"):
            print("Come on man. Just put in the right thing.")
            line8d = input("do you run (r), fight (f), or befriend (b)?")

        if line8d == "r":
            print("You turn and flee but the troll catches you after only three steps. you feel his enormous fangs sink into you and your lifeblood\nseeps onto the ground. The last thing you hear is the crunching sound of your own bones.\nYou are Dead.\n")
            Lives -= 1

        elif line8d == "f":
            print("You turn to face the charging troll and swing your fist at it's knee, the highest part of it you can reach.\nThe troll merely rips off the offending arm and lifts you into the air. You are slowly lifted into the troll's mouth and as you die from his immense flags ripping your flesh. The last sound you hear is the rending of your flesh and bone.\nYou are Dead.")
            Lives -= 1

        else:
            print("You turn and try to say something but the troll has shoved you in his mouth before you can even think.\n You die it agony as you are chewed by the blunt, bludgeoning molars of the troll. The last thing you hear is the snapping and crunching of your own bones.\nYou are Dead.")        
            Lives -= 1

else:
    line8d = input("You enter a long corridor. As you round a bend you suddenly encounter a troll! It glares at you and moves incredibly quickly and agressively towards you.\nYou can either run (r), fight with fists (f), or try to befriend it (b). What do you do?\n")
        
    while not(line8d == "r" or line8d == "f" or line8d == "b"):
        print("Come on man. Just put in the right thing.")
        line8d = input("do you run (r), fight (f), or befriend (b)?")

    if line8d == "r":
        print("You turn and flee but the troll catches you after only three steps. you feel his enormous fangs sink into you and your lifeblood\nseeps onto the ground. The last thing you hear is the crunching sound of your own bones.\nYou are Dead.\n")
        Lives -= 1

    elif line8d == "f":
        print("You turn to face the charging troll and swing your fist at it's knee, the highest part of it you can reach.\nThe troll merely rips off the offending arm and lifts you into the air. You are slowly lifted into the troll's mouth and as you die from his immense flags ripping your flesh. The last sound you hear is the rending of your flesh and bone.\nYou are Dead.")
        Lives -= 1

    else:
        print("You turn and try to say something but the troll has shoved you in his mouth before you can even think.\n You die it agony as you are chewed by the blunt, bludgeoning molars of the troll. The last thing you hear is the snapping and crunching of your own bones.\nYou are Dead.")        
        Lives -= 1


checkdead(Lives,Correct)

#Question #9

line9 = input("\n\n\n\n\n\nWhat species is Jabba the Hutt?\n")
if line9 == "hutt":
    print("Lol u gud boi")
    Correct += 1

elif line9 == "a hutt":
    print("guudisshhhh")
    Correct += 1

else:
    print("u smell horribull boi")
    Lives -= 1

checkdead(Lives,Correct)

#Question #10

line10 = input("\n\nAND FINALLY\nTHE FINAL QUESTION\nAM I COOL?\n\n")
while not(line10 == "y" or line10 == "n"):
    print("u r the suuper dummist dorkk in the whoel werld just stopp beeing dumm u dorky moron dumbutt.\n")
    line10 = input("Am I cool?\n")
if line10 == "y":
    print("u r thu bessssssst\n\n")
    Correct += 1

else:
    print("u r the worst u stupid moron!!!\n\n")
    Lives -= 1

checkdead(Lives,Correct)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCongrats, you've passed the test!\nYou had " + str(Lives) + " lives left.\nYour final score was " + str(Correct) + ".\n\n\n")
