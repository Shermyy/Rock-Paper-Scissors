import random as r
import time as t
print("Boss Fight vs Angry Garuda >=(")

Garuda = 50
Gardua_BaseDMG = 7
Garuda_Def = 5


You = 50
You_BaseDmg = 5
You_Defense = 3









turn = True

def roll_system():

    roll = r.randint(1,5)


    return roll

def attack_system():


    if roll_system() < 2:
        print("Attack Failed")
        return False
    else:
        print("Attack Success!")
        return True



while Garuda != 0:
    if attack_system() and turn == True:
        Garuda = Garuda - You_BaseDmg
        print(f"Garuda took {You_BaseDmg} and is now at {Garuda}HP")
    elif attack_system() == False and turn == True:
        print("You missed.")
    else:
        print(roll_system())
        print("Dodged")
    t.sleep(.5)



print("Battle ended")
