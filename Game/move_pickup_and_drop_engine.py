


NORTH = "go north"
SOUTH = "go south"
EAST = "go east"
WEST = "go west"

Inventory = []
HeldItem = "fist"
Location = 1





# Input Checker for GetInput
def InputChecker(Text,ValidInput):
    Input = input(Text + "\n").lower()
    while ValidInput.count(Input) == 0:
        Input = input("Please enter a valid input\n")
    return Input


# Move, Pick up, and Drop engine
def GetInput(Nflag,Sflag,Eflag,Wflag,Text,ValidInput):
    DirFail = True

    Input = InputChecker(Text,ValidInput)

    while DirFail == True:
        if Input == NORTH and Nflag == False:
            DirFail = True
            Input = InputChecker("You can't go there",ValidInput)

        elif Input == SOUTH and Sflag == False:
            DirFail = True
            Input = InputChecker("You can't go there",ValidInput)

        elif Input == EAST and Eflag == False:
            DirFail = True
            Input = InputChecker("You can't go there",ValidInput)
            
        elif Input == WEST and Wflag == False:
            DirFail = True
            Input = InputChecker("You can't go there",ValidInput)

        else:
            return Input
            DirFail = False
    

if Location == 1:
    Nflag = True
    Sflag = True
    Eflag = False
    Wflag = False
    item = "pillow"
    Text = "You are in a room with a door to the north and a table with a sword on it. What do you do?"
    ValidInput = [NORTH,SOUTH,EAST,WEST,"pick up sword","drop " + item]
    Input = GetInput(Nflag,Sflag,Eflag,Wflag,Text,ValidInput) 
    