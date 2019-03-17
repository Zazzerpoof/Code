        #Basic Variables and Lists

cmdList = []
dirfail = True
N = True
S = True
E = True
W = True
Position = 1
DirInput = 0
text = 0
error = 0

Inventory = []
Equipped = 0

NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"


        #Functions
#Get Input for nsew
def gifnsew(Text,ErrorMessage):
    DirectionInput = input(Text + "\n").lower()
    while not(DirectionInput == NORTH or DirectionInput == SOUTH or DirectionInput == EAST or DirectionInput == WEST):
        print(ErrorMessage)
        DirectionInput = input("\n").lower()
    return DirectionInput

#Forward Backward Left Right
def nsew(Nflag, Sflag, Eflag, Wflag, Text, ErrorMessage, DirectionFailMessage):
    DirFail = True
    

    DirectionInput = gifnsew(Text,ErrorMessage)

    while DirFail == True:


        if DirectionInput == NORTH and Nflag == True:
            DirFail = False
            return DirectionInput

        elif DirectionInput == SOUTH and Sflag == True:
            DirFail = False
            return DirectionInput

        elif DirectionInput == EAST and Eflag == True:
            DirFail = False
            return DirectionInput

        elif DirectionInput == WEST and Wflag == True:
            DirFail = False
            return DirectionInput

        else:
           print(DirectionFailMessage)
           DirectionInput = gifnsew(Text,ErrorMessage)
           
           #DirectionInput = input(Text + "\n")
           DirFail = True

#Get Valid Input
def gvi(cmdList,Text):
    Input = input(Text + "\n").lower()
    Input = input("Please enter a valid command\n")
    return Input

#Command executer


while Position != 7:

    
    Nflag = ["Space taker Upper",True,True,False,True,True,True,False,False,False,True,True,False]
    Sflag = ["Space taker Upper",False,True,True,False,True,True,False,False,True,False,False,True]
    Eflag = ["Space taker Upper",False,False,True,False,False,True,False,False,True,False,True,True]
    Wflag = ["Space taker Upper",False,False,True,False,True,False,False,False,True,True,False,False]
    Text = ["Space taker Upper","You are in a dusty room with a skeleton leaning against the wall. To the north is a door.","You are in a hallway. To the north is more hallway and to the south is a door.","You arrive at a T intersection. The South, East, and West are all hallways.","You are in an empty room. To the north there is a door.","You arrive at a bend in the hallway. To the North and West are hallways but there is a door to the south.","You arrive in a hallway that continues South with a door to the East and North.","U win BOI","You walk into a room and the floor crumbles beneath you. You fall into a deep crevasse and smash onto the rocky floor.\nYou are Dead.","You arrive in a hallway with a passage to the west, south, and east.","You are in a passage that continues to the north and west.","You are in a passage that continues to the North and East.","You are in a passage that continues to the South and East."]
    Error = "Please enter a valid command; either (n) (s) (e) (w)"
    DirFailErrorMessage = "There is a wall there"
    Nposition = ["Space taker Upper",2,3,3,5,6,8,7,8,9,9,12,12]
    Sposition = ["Space taker Upper",1,1,2,4,4,5,7,8,10,10,12,12]
    Eposition = ["Space taker Upper",1,2,5,4,5,7,7,8,3,10,10,9]
    Wposition = ["Space taker Upper",1,2,9,4,3,6,7,8,12,11,10,12]
    Deathflag = ["Space taker Upper",False,False,False,False,False,False,False,True,False,False,False,False]

    response = nsew(Nflag[Position],Sflag[Position],Eflag[Position],Wflag[Position],Text[Position],Error,DirFailErrorMessage)
    Pos = Position

    if Position == 8:
        print("You walk into a room and the floor crumbles beneath you. You fall into a deep crevasse and smash onto the rocky floor.\nYou are Dead.")
        break
    else:
        pass

    if response == SOUTH:
        Position = Sposition[Pos]

    elif response == EAST:
        Position = Eposition[Pos]

    elif response == WEST:
        Position = Wposition[Pos]

    else:
        Position = Nposition[Pos]    

if Pos == 8:
    exit()
else:
    pass

#print("You walk out of the side of the giant ancient house you were in. You hear a deep thundering sound.\nTunring around, you watch as the whole structure begins to crumple in on itself.\nYou stand dumbstruck as the whole building collapses into nothing but a pile of rubble.\nTurning, you walk away from the heap and go on your merry way down a nearby path.\nU win boi")

#Input checker for part two
def InputChekks(ValidInput):
    Input = input("\n").lower()
    while ValidInput.count(Input) == 0:
        Input = input("Please input a valid command\n")

    return Input

''' 
        if ValidInput.count(Input) > 0:
            return Input
    
        else:
            Input = input("Please input a valid command\n")
'''

print("You emerge from a huge spruce door in the side of a mountain. You look around and see a large aztec temple \noff to the left and an old cottage to the right. Where do you go?")

ValidInput = ["right","left","r","l"]
reply = InputChekks(ValidInput)

if reply == "right" or reply == "r":
    print("You walk over to the cottage. It sits slightly askew on the uneven terrain, \nwith the remains of a garden overrun by weeds off to the side. You see that the door has been knocked slightly ajar \nand several windows have been broken in. Would you rather investigate the garden or try to open the door?")
    ValidInput = ["investigate the garden","garden","the garden","open the door","door","the door","try to open the door"]
    reply = InputChekks(ValidInput)

    if reply == "investigate the garden" or reply == "garden" or reply == "the garden":
        print("You walk over to the garden and jump over the crumbling fence. When you land on the other side \nyou fall through the floor into a cave and land with a crunch. As both of your legs are broken, \nyou are unable to move and die of blood loss.\nYou are dead.")
        exit()

    else:
        print("You approach the huge old solid spruce door and slowly begin to open it.\nAs you move it, the old rusty hinges snap and the huge door falls onto you. \nYou hear your legs snap and your head cracks onto the floor. The last thing you see is an old hunchbacked man wheeze,\"I have crippling depression...\"\nYou are Dead")
        exit()

else:
    print("You walk")



