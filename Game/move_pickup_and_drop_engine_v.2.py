import time

Inventory = []
HeldItem = "fist"
location = 1
ValidInput = ["go","drop","grab","hold","list"]
ValidGo = ["north","south","east","west"]
Text = "Say Something"

Pickupable1 = ["sword","lel","poison"]
Pickupable2 = ["lollipop"]
Pickupable3 = ["trollface","dirt","death","lol","ugliness"]
Pickupable4 = ["weird_younger_brother", "severed_head"]
Pickupable5 = []

'''
Nflag = 0
Sflag = False
Eflag = False
Wflag = False
'''
'''
RawInput = input("say something\n").lower()
Input = RawInput.split()
while ValidInput.count(Input[0]) == 0 or ValidGo.count(Input[1]) == 0:
    RawInput = input("Please enter a valid command\n").lower()
    Input = RawInput.split()

print("hi")


RawInput = input("say something\n").lower()
Input = RawInput.split()
'''

def InputCheck1(ValidInput):
    RawInput = input("").lower()
    Input = RawInput.split()
    while len(Input) == 0:
        RawInput = input("Please enter a valid command\n").lower()
        Input = RawInput.split()
    while ValidInput.count(Input[0]) == 0:
        RawInput = input("Please enter a valid command\n").lower()
        Input = RawInput.split()
    return Input


def InputCheck2(ValidInput,Text,Pickupable,Inventory):
    Fail = True
    print(Text)
    
    while Fail == True:  
        Input = InputCheck1(ValidInput)    
        if Input[0] == "list" and len(Input) == 1:
            Lelz = ", ".join(Inventory)
            print(Lelz + "      (press enter to continue)")

        if Input[0] == "go" and len(Input) == 2:
            if ValidGo.count(Input[1]) > 0:
                return Input 
                break
            else:
                print("\"" + Input[1] + "\" isn't a direction")

        elif Input[0] == "drop" and len(Input) == 2:
            if Inventory.count(Input[1]) > 0:
                return Input
                break

            else:
                print("You don't have a " + Input[1])

        elif Input[0] == "hold" and len(Input) == 2:
            if Inventory.count(Input[1]) > 0:
                return Input 
                break

            else:
                print("You don't have a " + Input[1])

        elif Input[0] == "grab" and len(Input) == 2:
            if Pickupable.count(Input[1]) > 0:
                return Input
                break
            
            else:
                print("There isn't a " + Input[1] + " in the room")

        elif len(Input) == 1 and Input[0] != "list":
            print("Too few parameters")

        elif len(Input) > 2:
            print("Too many parameters")
        
        else:
            pass

def GetInput(ValidInput,Text,Pickupable,Inventory,Nflag,Sflag,Eflag,Wflag):
    Fail = True
    
    while Fail == True:
        Input = InputCheck2(ValidInput,Text,Pickupable,Inventory)    
        if Input[0] == "go" and Input[1] == "north" and Nflag == True :
            return Input
            Fail = False

        elif Input[0] == "go" and Input[1] == "south" and Sflag == True:
            return Input
            Fail = False

        elif Input[0] == "go" and Input[1] == "west" and Wflag == True:
            return Input
            Fail = False

        elif Input[0] == "go" and Input[1] == "east" and Eflag == True:
            return Input
            Fail = False

        elif Input[0] == "grab":
            Inventory.append(Input[1])
            print("Grabbed " + Input[1])
            return Input
            Fail = False

        elif Input[0] == "drop":
            Inventory.remove(Input[1])
            print("Dropped " + Input[1])
            return Input
            Fail = False

        elif Input[0] == "hold":
            HeldItem = Input[1]
            return Input
            Fail = False

        else:
            print("You can't go there")
            Fail = True

while True:
    if location == 1:
        Nflag = True
        Sflag = False
        runs = 0
        Eflag = False
        Wflag = False
        ThingCount = len(Pickupable1)
        if ThingCount == 0:
            Text = "You are in an empty room with a door to the north."

        elif ThingCount == 1:
            Text = "You are in a room with a door to the north. The only thing in the room is a " + Pickupable1[0]
        
        else:
            Text = "You are in an room with a door to the north. The things in the room are: a " + ", a ".join(Pickupable1)
        
        Input = GetInput(ValidInput,Text,Pickupable1,Inventory,Nflag,Sflag,Eflag,Wflag)
    
        if Input[0] == "go":
            if Input[1] == "north":
                location = 2

            elif Input[1] == "south":
                location = 1

            elif Input[1] == "east":
                location = 1

            elif Input[1] == "west":
                location = 1

            else:
                print("I'm sorry but there has been an Error.")
        
        elif Input[0] == "drop":
            Pickupable1.append(Input[1])

        elif Input[0] == "grab":
            Pickupable1.remove(Input[1])
        
        else:
            pass

    if location == 2:
        Nflag = True
        Sflag = True
        runs = 0
        Eflag = True
        Wflag = False
        ThingCount = len(Pickupable2)
        if ThingCount == 0:
            Text = "You are in an empty room with a door to the north, east, and south."

        elif ThingCount == 1:
            Text = "You are in a room with doors to the north, east, and south. The only thing in the room is a " + Pickupable2[0]
        
        else:
            Text = "You are in an room with doors to the north, east, and south. The things in the room are: a " + ", a ".join(Pickupable2)
        
        Input = GetInput(ValidInput,Text,Pickupable2,Inventory,Nflag,Sflag,Eflag,Wflag)
    
        if Input[0] == "go":
            if Input[1] == "north":
                location = 3

            elif Input[1] == "south":
                location = 1

            elif Input[1] == "east":
                location = 5

            elif Input[1] == "west":
                location = 2

            else:
                print("I'm sorry but there has been an Error.")
        
        elif Input[0] == "drop":
            Pickupable2.append(Input[1])

        elif Input[0] == "grab":
            Pickupable2.remove(Input[1])
        
        else:
            pass


    if location == 3:
        Nflag = False
        Sflag = True
        runs = 0
        Eflag = True
        Wflag = False
        ThingCount = len(Pickupable3)
        if ThingCount == 0:
            Text = "You are in an empty room with a door to the east and south."

        elif ThingCount == 1:
            Text = "You are in a room with doors to the east and south. The only thing in the room is a " + Pickupable3[0]
        
        else:
            Text = "You are in an room with doors to the east and south. The things in the room are: a " + ", a ".join(Pickupable3)
        
        Input = GetInput(ValidInput,Text,Pickupable3,Inventory,Nflag,Sflag,Eflag,Wflag)
    
        if Input[0] == "go":
            if Input[1] == "north":
                location = 3

            elif Input[1] == "south":
                location = 2

            elif Input[1] == "east":
                location = 4

            elif Input[1] == "west":
                location = 3

            else:
                print("I'm sorry but there has been an Error.")
        
        elif Input[0] == "drop":
            Pickupable3.append(Input[1])

        elif Input[0] == "grab":
            Pickupable3.remove(Input[1])
        
        else:
            pass    
    

    if location == 4:
        Nflag = False
        Sflag = True
        runs = 0
        Eflag = False
        Wflag = True
        ThingCount = len(Pickupable4)
        if ThingCount == 0:
            Text = "You are in an empty room with a door to the west and south."

        elif ThingCount == 1:
            Text = "You are in a room with doors to the west and south. The only thing in the room is a " + Pickupable4[0]
        
        else:
            Text = "You are in an room with doors to the west and south. The things in the room are: a " + ", a ".join(Pickupable4)
        
        Input = GetInput(ValidInput,Text,Pickupable4,Inventory,Nflag,Sflag,Eflag,Wflag)
    
        if Input[0] == "go":
            if Input[1] == "north":
                location = 4

            elif Input[1] == "south":
                location = 5

            elif Input[1] == "east":
                location = 4

            elif Input[1] == "west":
                location = 3

            else:
                print("I'm sorry but there has been an Error.")
        
        elif Input[0] == "drop":
            Pickupable4.append(Input[1])

        elif Input[0] == "grab":
            Pickupable4.remove(Input[1])
        
        else:
            pass    


    if location == 5:
        Nflag = True
        Sflag = False
        runs = 0
        Eflag = False
        Wflag = True
        ThingCount = len(Pickupable5)
        if ThingCount == 0:
            Text = "You are in an empty room with a door to the west and north."

        elif ThingCount == 1:
            Text = "You are in a room with doors to the west and north. The only thing in the room is a " + Pickupable5[0]
        
        else:
            Text = "You are in an room with doors to the west and north. The things in the room are: a " + ", a ".join(Pickupable5)
        
        Input = GetInput(ValidInput,Text,Pickupable5,Inventory,Nflag,Sflag,Eflag,Wflag)
    
        if Input[0] == "go":
            if Input[1] == "north":
                location = 4

            elif Input[1] == "south":
                location = 5

            elif Input[1] == "east":
                location = 5

            elif Input[1] == "west":
                location = 2

            else:
                print("I'm sorry but there has been an Error.")
        
        elif Input[0] == "drop":
            Pickupable5.append(Input[1])

        elif Input[0] == "grab":
            Pickupable5.remove(Input[1])
        
        else:
            pass    













































































































            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
