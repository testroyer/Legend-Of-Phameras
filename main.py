"""
========================================================================
                       LEGEND OF PHAMERAS
                        (Demo / Concept)
                created by testroyer and phonem
                     10 March 2022, 16:47:16
========================================================================
"""

#   /$$                                                /$$                 /$$$$$$        /$$$$$$$ /$$                                                               
#  | $$                                               | $$                /$$__  $$      | $$__  $| $$                                                               
#  | $$       /$$$$$$  /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$        /$$$$$$| $$  \__/      | $$  \ $| $$$$$$$  /$$$$$$ /$$$$$$/$$$$  /$$$$$$  /$$$$$$ /$$$$$$  /$$$$$$$
#  | $$      /$$__  $$/$$__  $$/$$__  $| $$__  $$/$$__  $$       /$$__  $| $$$$          | $$$$$$$| $$__  $$|____  $| $$_  $$_  $$/$$__  $$/$$__  $|____  $$/$$_____/
#  | $$     | $$$$$$$| $$  \ $| $$$$$$$| $$  \ $| $$  | $$      | $$  \ $| $$_/          | $$____/| $$  \ $$ /$$$$$$| $$ \ $$ \ $| $$$$$$$| $$  \__//$$$$$$|  $$$$$$ 
#  | $$     | $$_____| $$  | $| $$_____| $$  | $| $$  | $$      | $$  | $| $$            | $$     | $$  | $$/$$__  $| $$ | $$ | $| $$_____| $$     /$$__  $$\____  $$
#  | $$$$$$$|  $$$$$$|  $$$$$$|  $$$$$$| $$  | $|  $$$$$$$      |  $$$$$$| $$            | $$     | $$  | $|  $$$$$$| $$ | $$ | $|  $$$$$$| $$    |  $$$$$$$/$$$$$$$/
#  |________/\_______/\____  $$\_______|__/  |__/\_______/       \______/|__/            |__/     |__/  |__/\_______|__/ |__/ |__/\_______|__/     \_______|_______/ 
#                     /$$  \ $$                                                                                                                                      
#                    |  $$$$$$/                                                                                                                                      
#                     \______/                                                                                                                                       

"""
def ToDo():
    !Creates a new inventory file when creating
    +work()
    !buying the same food twice ---> Swept under carpet
    +fight()
"""
"""
comment: this project looks cool
-Sir Raus0n
"""
"""
Array documentation:

[
    (price,) -> Price at the shop.
    value, -> Value of an item
    state ->if 0:
                eatable
            if 1:
                weapon
            if 2:
                wearable
            if 21:
                special item

]
"""

#dumped variables
#The formula that will be used laeter on to calculate the damage which will be inflicted to enemy.
damageCalc = lambda base, attack ,defense : (base + (base * (attack / 100))) * ((100 - defense) / 100)

#Imports
from math import pi
from classes.character import Character
import sys
import time
import json


#Loads json data for inventory
with open("./Json-Files/inventory.json" , "r") as f:             
    data = json.load(f)

#Loads json data for shopping
with open("./Json-Files/shop.json" , "r") as f:             
    shop = json.load(f)

#Saver function made for saving json file. I didn't make a copy of this for the shop.json because it is unnecessary
def json_saver(json_string):                                
    with open("./Json-Files/inventory.json" , "w+") as c:
        c.write(json_string)

def character_lister(data):
    print("<Available characters:")
    for characters in data[0]:
        print(characters)

#Makes you choose a character at the start. While is needed for try-expect
while True:        
    try:
        if data == [{}]:
            print("<You don't have any characters. You must create one. Please enter a name for your character")
            new_character = input(">")
            data[0][new_character] = {
                "isArmorEquipped" : False,
                "isWeaponEquipped": False,
                "AttackBase" : 15,
                "DefenseBase" : 20,
                "maxHealth" : 100,
                "Health" : 100,
                "Body":{
                    
                },
                "Inventory" : {
                    "Coins" : [0 , 21]
                }   
            
            }
            player = data[0][new_character]
            inventory = data[0][new_character]["Inventory"]
            player_body = data[0][new_character]["Body"]    #I made a body for wearing armor
            character = Character(player = player ,player_inventory = inventory , player_body=player_body)
            json_string = json.dumps(data , indent=4)
            json_saver(json_string=json_string)
        print("<Character created successfully")
        character_lister(data)
        selected_character = input("<Select Character: \n>")   
        player , inventory , player_body = data[0][selected_character] , data[0][selected_character]["Inventory"], data[0][selected_character]["Body"]
        
        break
    except KeyError:
        print("<Please enter a valid character name")

#Created for later business. I'm thinking of an error message like "Please write a valid command". Seems it could be done with a for loop checking if the command startswith or just use else.
command_array = [">list" ,">work", ">coins", ">help", ">equip", ">unequip" , ">select", ">buy" , ">new character" , ">drop" , ">pick" , ">exit" , ">save" , ">info" , ">health" , ">list body" , ">selfharm" , ">delete character"]          

character = Character(player = player , player_inventory = inventory , player_body=player_body)
print("<Boot successfull")

#I believe I can make this one function and then import it
#Checks input every time. I find it a bit dumb to make it this way
while True:  
    if character.display_health() == 0:
        print("<You're dead. Game Over. If you want to continue from your last save simply restart the game.")
        sys.exit("<Game exit.")

    the_input = input()

    #Sorts command array in alphabetical order and prints it
    if the_input == ">help":    
        for commands in sorted(command_array):
            print(commands)

    elif the_input == ">list body":
        if character.list_body() == []:
            print("<There is nothing on body")
        else:
            for item in character.list_body():
                print(item)

    #Displays your coins             
    elif the_input == ">coins":
        character_coins = character.list_coins()
        print(f"You have {character_coins} coins.")

    #It does what it does, lists.
    elif the_input  == ">list":
        if character.character_inventory() != []:            
            character.list_inventory()
        else:
            print("<You have nothing.")

    elif the_input == ">defense":
        print(f"Your defense value is {character.get_defense()}.")

    elif the_input == ">attack":
        print(f"Your attack value is {character.get_attack()}.")

    elif the_input.startswith(">select"):          #Created for character selection. MAYBE: Write a function that lists characters instead of inventory. 
        try:
            character_selection = the_input[8:]
            inventory = data[0][character_selection]["Inventory"]
            player = data[0][character_selection]
            player_body = data[0][character_selection]["Body"]
            character = Character(player=player,player_inventory=inventory, player_body=player_body)
            print(f"<{character_selection} selected")
        except KeyError:
            print("<Please select a valid character name")

    #work   -> Gives you random or entered amount of coins. A value between 1 and 20. maybe we can add a delay or something like that.
    elif the_input.startswith(">work"):
        try:        
            work_time = int(the_input[6:])
            time.sleep(work_time)
            gain = round(work_time*pi)
            player_inventory = character.character_inventory()
            player_inventory["Coins"][0] += gain 
            print(f">You gained {gain} coins")
        except ValueError:
            print(">Please determine a time to work for.")

    #Equips an item. I must add a property which makes an item equipable or not.
    elif the_input.startswith(">equip"):             
        try:
            item = the_input[7:]
            player_inventory = character.character_inventory()
            if player_inventory[item][1] == 2 and player["isArmorEquipped"] == False:
                character.equip_armor(item)
                player["isArmorEquipped"] = True
                print(f"<{item} has been worn.")
                continue
            if player_inventory[item][1] == 1 and player["isWeaponEquipped"] == False:
                character.equip_item(item)
                player["isWeaponEquipped"] = True
                print(f"<Equipped {item}")
                continue
            elif player_inventory[item][1] == 2 and player["isArmorEquipped"] == True:
                print("<You already have an armor equipped.")
                continue
            elif player_inventory[item][1] == 1 and player["isWeaponEquipped"] == True:
                print("<You already have an weapon equipped.")
                continue
            else:
                print("<Please, you can't equip this")
                continue
        except KeyError:
            print("<Please select a valid item")

    #Same thing. Unequips an item. I must add a property which makes an item equipable or not.
    elif the_input.startswith(">unequip"):             
        try:
            item = the_input[9:]
            player_body = character.character_body()
            if player_body[item][1] == 2 and player["isArmorEquipped"] == True:
                character.unequip_armor(item)
                player["isArmorEquipped"] = False
                print(f"<Removed {item}")
                continue
            if player_body[item][1] == 1 and player["isWeaponEquipped"] == True:
                character.unequip_item(item)
                player["isWeaponEquipped"] = False
                print(f"<Unequipped {item}")
                continue
            else:
                print("<Please, you can't un-equip this")
                continue
        except KeyError:
            print("<Please select a valid item")

    #Eats a food. Nearly the whole command was written in the Character class. 
    elif the_input.startswith(">eat"):
        try:
            food = the_input[5:]
            character.eat(food)
        except KeyError:
            print("Please select a valid item")

    #health -> displays health
    elif the_input == ">health":
        print(f"Health is {character.display_health()}")

    #self_harm -> Self harm made for testing
    elif the_input.startswith(">selfharm"):
        try:
            harm_value = int(the_input[10::])
            character.harm(harm_value)
            print(f"Health is now {character.display_health()}")
        except:
            print("<An error occured.")


    elif the_input == ">shop":
        print("<These are the items on sale:")
        shop_hash = shop[0]
        for items in shop_hash:
            print(f"{items} : {shop_hash[items][0]}")

    # Buys an item from shop.json. First item in arrays is the price and the second one is the value.
    elif the_input.startswith(">buy"):
        try:
            the_item_to_be_bought = the_input[5:]
            character_inventory = character.character_inventory()
            if the_item_to_be_bought in character_inventory:
                print("You already have this item")
                continue
            if character_inventory["Coins"][0] > shop[0][the_item_to_be_bought][0]:
                values = [shop[0][the_item_to_be_bought][1] , shop[0][the_item_to_be_bought][2]]
                character.pick_item(the_item_to_be_bought , values)
                character_inventory["Coins"][0] -= shop[0][the_item_to_be_bought][0]
                print(f">{the_item_to_be_bought} is successfully bought.")
            else:
                print("You don't have enough coins.")
        except KeyError:
            print("<That item doesn't exist at any of our shops.")

    #delete character -> If entered nothing next to ">delete character" displays an error message else if there is an entered character name deletes that character. Makes sure to get confirmation.
    elif the_input.startswith(">delete character"):
        try:
            yes_or_no = input("<Are you sure Y/N \n>")
            if yes_or_no.lower == "n":
                continue
            else:
                pass
            character_to_be_deleted = the_input[18:]
            data[0].pop(character_to_be_deleted)
            character_selection = input("Select a character \n>")
            inventory = data[0][character_selection]["Inventory"]
            player = data[0][character_selection]
            player_body = data[0][character_selection]["Body"]
            character = Character(player=player,player_inventory=inventory, player_body=player_body)
            print(f"<{character_selection} selected")
        except KeyError:
            print("That character doesn't exist")
        except:
            print("An error occured.")

    #Character creator, creates a new character and saves the inventory file.
    elif the_input.startswith(">new character"):
        new_character = the_input[15:]
        #Character initializer
        data[0][new_character] = {
            "isArmorEquipped" : False,
            "isWeaponEquipped": False,
            "AttackBase" : 15,
            "DefenseBase" : 20,
            "maxHealth" : 100,
            "Health" : 100,
            "Body":{
                
            },
            "Inventory" : {
                "Coins" : [0 , 21]
            }   
            
        }
        player = data[0][new_character]
        inventory = data[0][new_character]["Inventory"]
        player_body = data[0][new_character]["Body"]    #I made a body for wearing armor
        character = Character(player = player ,player_inventory = inventory , player_body=player_body)
        json_string = json.dumps(data , indent=4)
        json_saver(json_string=json_string)
        print("<Character created successfully")

    #Drops an item. I disabled dropping coins because it's dumb to drop coins
    elif the_input.startswith(">drop"):
        try:
            the_item = the_input[6:]
            if the_item == "Coins":
                print("<Are you mad! Why are you dropping your coins?")
                continue
            character.drop_item(item = the_item)
        except KeyError:
            print("<Please enter a valid item to drop")

    #Exiting function
    elif the_input == ">exit":                                              
        print("<Are you sure? Any un-saved changes will be lost Y/N")
        yes_or_no = input(">")
        if yes_or_no.lower() == "y":
            sys.exit("<Game exit")
        elif yes_or_no.lower() == "n":
            continue
        else:
            print("Please enter a valid parameter.")

    #Saving function    
    elif the_input == ">save":
        json_string = json.dumps(data , indent=4)
        json_saver(json_string=json_string)
        print(">Game saved successfully")

    #Displays information about the character
    elif the_input.startswith(">info"):   
        try:
            the_item = the_input[6:]
            character.item_info(item = the_item)
        except KeyError:
            print("<Please enter a valid item to show info of.")
