import random
import time

LegendaryWeapons = ["War Hammer","Double Sabre", "Double Sword","Hammer Axe", "Supersword","Shielding Glaive","Heavy Rapier"]
LegendaryArmor = ["Super Helmet", "Super Chestplate","Super Leggings","Super Armguards"]
EpicWeapons = ["Battleaxe","Trident-Axe","Curved Sabre","Level 3 Shield","Sabre","Poleaxe","Flail","Trident","Punch-Axe","Glaive","War Rake"]
EpicArmor = ["Heavy Steel Helmet", "Heavy Steel Chestplate", "Heavy Steel Leggings", "Heavy Steel Armguards","Heavy Iron Helmet", "Heavy Iron Chestplate", "Heavy Iron Leggings", "Heavy Iron Armguards"]
RareWeapons = ["Greatclub","3 Foot Sword","2 1/2 Foot Sword","Split Dagger","Level 2 Shield","Lance", "4 Foot Sword","Quarterstaff"]
RareArmor = ["Iron Helmet", "Iron Chestplate", "Iron Armguards", "Iron Leggings","Steel Helmet", "Steel Chestplate", "Steel Armguards", "Steel Leggings","Plate Iron Helmet", "Plate Iron Chestplate", "Plate Iron Armguards", "Plate Steel Leggings"]
CommonWeapons = ["Sword Breaker Dirk", "Sword Breaker Dagger", "Wood Plank", "Spear", "Dagger", "Level 1 Sheild", "Axe", "Club", "Handaxe", "Mace", "2 Foot Sword", "Double Axe", "Buckler"]
CommonArmor = ["Leather Helmet", "Leather Chestplate", "Leather Armguards", "Leather Leggings","Studded Leather Helmet", "Studded Leather Chestplate", "Studded Leather Armguards", "Studded Leather Leggings","Chain Helmet", "Chain Chestplate", "Chain Leggings","Chain Armguardss"]

Room = ""
ChestsInRoom = 0
DragonInRoom = 0

def GenerateRoom():
    ChestsInRoom = 0
    DragonInRoom = 0
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAre you ready to generate a room?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    RawNumber = random.randint(1,101)
    if RawNumber > 0 and RawNumber < 21:
        Room = "2x2"
        RawNumber = random.randint(1,6)
        if RawNumber == 5:
            ChestsInRoom = 1
        else:
            pass
    elif RawNumber > 20 and RawNumber < 41:
        Room = "3x3"
        RawNumber = random.randint(1,21)
        if RawNumber < 10:
            ChestsInRoom = 1
        else:
            pass
    elif RawNumber > 40 and RawNumber < 61:
        Room = "4x4"
        RawNumber = random.randint(1,6)
        if RawNumber < 5:
            ChestsInRoom = 1
        else:
            pass
    elif RawNumber > 60 and RawNumber < 71:
        Room = "5x5"
        RawNumber = random.randint(1,5)
        if RawNumber == 4:
            ChestsInRoom = 2
        else:
            ChestsInRoom = 1
    elif RawNumber > 70 and RawNumber< 76:
        Room = "6x6"
        RawNumber = random.randint(1,6)
        if RawNumber < 5:
            ChestsInRoom = 2
        else:
            ChestsInRoom = 1
    elif RawNumber > 75 and RawNumber < 86:
        Room = "Armory"
        RawNumber = random.randint(1,21)
        if RawNumber < 10:
            ChestsInRoom = 3
        else:
            ChestsInRoom = 2
    elif RawNumber > 85 and RawNumber < 91:
        Room = "Treasury"
        RawNumber = random.randint(1,21)
        if RawNumber < 10:
            ChestsInRoom = 4
        else:
            ChestsInRoom = 3
    elif RawNumber > 90 and RawNumber < 100:
        Room = "Infirmary"
        RawNumber = random.randint(1,21)
        if RawNumber < 10:
            ChestsInRoom = 3
        else:
            ChestsInRoom = 2
    else:
        Room = "10x10"
        ChestsInRoom = 5


    RawNumber = random.randint(0,8)
    if RawNumber == 8:
        RawNumber = random.randint(1,11)
        if RawNumber > 0 and RawNumber < 7:
            DragonInRoom = 1
        elif RawNumber > 6 and RawNumber < 10:
            DragonInRoom = 2
        else:
            DragonInRoom = 3

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if ChestsInRoom > 0 and DragonInRoom > 0:
        input("You have a " + Room + " room with " + str(ChestsInRoom) + " chests and a level " + str(DragonInRoom) + " dragon in it.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    elif DragonInRoom > 0 and ChestsInRoom == 0:
        input("You are in a " + Room + " room with a level " + str(DragonInRoom) + " dragon in it.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    elif ChestsInRoom > 0 and DragonInRoom == 0:
        input("You are in a " + Room + " with " + str(ChestsInRoom) + " chests in it.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    else:
        input("You are in a " + Room + " room with no chests in it.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def isroom(distance):
    param = 10 - distance
    RawNumber = random.randint(1,11)
    if RawNumber > param:
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou get a Room\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        RawNumber = random.randint(1,5)
        if RawNumber == 1:
            input("\n\n\n\n\n\n\n\n\n\nYou get a hallway that curves to the left\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        elif RawNumber == 2:
            input("\n\n\n\n\n\n\n\n\n\nYou get a hallway that curves to the right\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        elif RawNumber == 3:
            input("\n\n\n\n\n\n\n\n\n\nYou get a T intersection hallway\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        else:
            input("\n\n\n\n\n\n\n\n\n\nYou get a crossroads hallway\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
Item = ""
Rarity = "Common"
def OpenChest():
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAre you ready to open a chest?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    RawNumber = random.randint(1,21)
    print(RawNumber)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading..\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    if RawNumber == 20:
        Rarity = "Legendary"
    elif RawNumber < 20 and RawNumber > 16:
        Rarity = "Epic"
    elif RawNumber > 10 and RawNumber < 17:
        Rarity = "Rare"
    else:
        Rarity = "Common"

    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have found a " + Rarity + " Chest! (Press enter to continue)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    RawNumber = random.randint(1,7)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading..\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print(RawNumber)

    if RawNumber == 6:
        Contents = "Healable"
    elif RawNumber == 4 or RawNumber == 5:
        Contents = "Armor"
    else:
        Contents = "Weapon"

    if Contents == "Armor":
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have found Armor in the chest! (Press enter to continue)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have found a " + Contents + " in the chest! (Press enter to continue)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading..\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(0.5)

    if Rarity == "Legendary":
        if Contents == "Weapon":
            RawNumber = random.randint(0,7)
            Item = LegendaryWeapons[RawNumber]
        elif Contents == "Armor":
            RawNumber = random.randint(0,4)
            Item = LegendaryArmor[RawNumber]
        else:
            Item = "Legendary Healable"
    elif Rarity == "Epic":
        if Contents == "Weapon":
            RawNumber = random.randint(0,11)
            Item = EpicWeapons[RawNumber]
        elif Contents == "Armor":
            RawNumber = random.randint(0,8)
            Item = EpicArmor[RawNumber]
        else:
            Item = "Epic Healable"

    elif Rarity == "Rare":
        if Contents == "Weapon":
            RawNumber = random.randint(0,7)
            Item = RareWeapons[RawNumber]
        elif Contents == "Armor":
            RawNumber = random.randint(0,12)
            Item = RareArmor[RawNumber]
        else:
            Item = "Rare Healable"

    elif Rarity == "Common":
        if Contents == "Weapon":
            RawNumber = random.randint(0,12)
            Item = CommonWeapons[RawNumber]
        elif Contents == "Armor":
            RawNumber = random.randint(0,12)
            Item = CommonArmor[RawNumber]
        else:
            Item = "Common Healable"
    else:
        pass
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou found a " + Item + " in the Chest!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
Input = " "


while True:
    Input = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat would you like to do? You can open a chest(O), Generate a room(G), Determine Hallway or Room(D), or quit(Q)?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n").lower()

    while Input != "o" and Input != "g" and Input != "q" and Input != "d":
        print("Please enter a valid command")
        Input = input("What would you like to do? You can open a chest(O), Generate a room(G), Determine Hallway or Room(D), or quit(Q)?\n").lower()
    if Input == "o":
        OpenChest()
    
    elif Input == "q":
        break

    elif Input == "d":
        distance = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHow far in hallways and rooms are you from start?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        distance = int(distance)
        isroom(distance) 

    else:
        GenerateRoom()
exit()
