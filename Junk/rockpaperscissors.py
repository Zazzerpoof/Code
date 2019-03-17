import random
import time
ValidInput = ["rock","paper","scissors","i hate you","u smell"]
def GetInput(ValidInput):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRock!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRock!\nPaper!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRock!\nPaper!\nScissors!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    Input = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRock!\nPaper!\nScissors!\nSHOOT!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n").lower()
    while ValidInput.count(Input) == 0:
        if Input == "no":
            input("Why not?\n")
            print("\nActually on second thought I don't really care.")
            time.sleep(1)
            Input = ("Just answer something right, OK?\n").lower()
        else:
            Input = input("Please enter a valid input\n").lower()
    return Input

playerPoints = 0
computerPoints = 0
input("Hello and Welcome to Rigged Rock Paper Scissors!\nWhen I say shoot type either rock, paper, or scissors.\nGot it?\n")

while computerPoints < 2 and playerPoints < 2:
    GoodInput = 0
    computerInput = 0
    Input = GetInput(ValidInput)

    if Input == "rock":
        GoodInput = "Rock"

    elif Input == "paper":
        GoodInput = "Paper"

    elif Input == "scissors":
        GoodInput = "Scissors"

    elif Input == "i hate you":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nI hate you too.\n\n\n\n\n\n\n\n\n\n\n")
        exit()

    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nI smell? Obviously you've never met yourself.\n\n\n\n\n\n\n\n\n")
        exit()

    RawComputerInput = random.randint(1,4)
    if RawComputerInput == 1:
        computerInput = "Rock"

    elif RawComputerInput == 2:
        computerInput = "Paper"

    else:
        computerInput = "Scissors"

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<You> " + GoodInput)
    print("<Computer> " + computerInput + "\n")
    if GoodInput == computerInput:
        input("You both chose the same thing! It's a tie! (press enter to continue)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif (GoodInput == "Rock" and computerInput == "Scissors") or (GoodInput == "Paper" and computerInput == "Rock") or (GoodInput == "Scissors" and computerInput == "Paper"):
        playerPoints += 1
        input("You won! (press enter to continue)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        computerPoints += 1
        input("You lost! Wow ur bad! (press enter to continue)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

if playerPoints == 2:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCongrats! You've won with " + str(playerPoints) +" victories and " + str(computerPoints) + " losses!\n")
    while True:
        print("*claps*")
        time.sleep(0.5)

else:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWow! You're horrible at this! You've failed with " + str(playerPoints) +" victories and " + str(computerPoints) + " losses!\n")
    while True:
        print("LOLOLOL")
        time.sleep(0.5)