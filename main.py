"""
========================================================================
                       LEGEND OF PHAMERAS
                        (Demo / Concept)
                created by testroyer and phonem
                     10 March 2022, 16:47:16
========================================================================
"""

#Command made with git

"""
def ToDo():
    -work()
    -delete character()
    -fight()
    -expand shops
    -armor
    -attack/armor/health value
    -character armor
    -a shop catalog would be useful
    -what if it starts without a character ???
    -shop stock ???
"""

#Imports
from character import Character
import sys
import json

#Loads json data for inventory
with open("inventory.json" , "r") as f:             
    data = json.load(f)

#Loads json data for shopping
with open("shop.json" , "r") as f:             
    shop = json.load(f)
    

#Makes you chose a character at the start. While is needed for try-expect
while True:        
    try:
        selected_character = input("<Select Character: \n>")   
        player , inventory = data[0][selected_character] , data[0][selected_character]["Inventory"]
        
        break
    except KeyError:
        print("<Please enter a valid character name")

#Created for later business. I'm thinking of an error message like "Please write a valid command". Seems it could be done with a for loop checking if the command startswith or just use else.
command_array = [">list" , ">select", ">buy" , ">new character" , ">drop" , ">pick" , ">exit" , ">save" , ">info" , ">health"]      

#Saver function made for saving json file. I didn't make a copy of this for the shop.json because it is unnescasary
def json_saver(json_string):                                
    with open("inventory.json" , "w") as f:
            f.write(json_string)
    

character = Character(player = player , player_inventory = inventory)
print("<Boot succesfull")

#I believe I can make this one function and then import it
#Checks input every time. I find it bit dump to make this this way
while True:                 
    the_input = input()

    #Sorts command array in alphabetical order and prints it
    if the_input == ">help":    
        for commands in sorted(command_array):
            print(commands)

    #It does what it does, lists.
    elif the_input  == ">list":               
        character.list_inventory()    

    elif the_input.startswith(">select"):                   #Created for character selection. MAYBE: Write a function that lists characters insted of inventory. 
        try:
            character_selection = the_input[8:]
            inventory = data[0][character_selection]
            character = Character(player_inventory=inventory)
            print(f"<{character_selection} selected")
        except KeyError:
            print("<Please select a valid character name")

    #work   -> Gives you random or entered amount of coins. A value between 1 and 20. maybe we can add a delay or something like that.

    #health -> displays health
    elif the_input == ">health":
        print(character.display_health())

    #self_harm -> Self harm made for testing
    elif the_input == ">selfharm":
        character.harm(10)

    # Buys an item from shop.json. First item in arrays is the price the second is the value.
    elif the_input.startswith(">buy"):
        try:
            the_item_to_be_bought = the_input[5:]
            character_inventory = character.character_inventory()
            if character_inventory["Coins"] > shop[0][the_item_to_be_bought][0]:
                character.pick_item(the_item_to_be_bought , shop[0][the_item_to_be_bought][1])
                character_inventory["Coins"] -= shop[0][the_item_to_be_bought][0]
        except KeyError:
            print("<That item doesn't exists at any one of our shops.")

    #delete character -> If entered nothing next to ">delete character" displays a error message else if there is an entered character name deletes that character. Makes sure to get confirmation.
    elif the_input.startswith(">delete character"):
        character_to_be_deleted = the_input[17:]

    elif the_input.startswith(">new character"):
        new_character = the_input[15:]
        data[0][new_character] = {
            "Health" : 100,
            "Inventory" : {
                "Coins" : 0
            }   
            
        }
        inventory = data[0][new_character]["Inventory"]
        character = Character(player = player ,player_inventory = inventory)
        json_string = json.dumps(data , indent=4)
        json_saver(json_string=json_string)
        print("<Character created succesfully")

    elif the_input.startswith(">drop"):         #Drops an item. I disabled dropping coins because it's dumb to drop coins
        try:
            the_item = the_input[6:]
            if the_item == "Coins":
                print("<Are you mad ? Why are you dropping your coins")
                continue
            character.drop_item(item = the_item)
        except KeyError:
            print("<Please anter a valid item to drop")

    #Exiting function
    elif the_input == ">exit":                                              
        print("<Are you sure ? Any un-saved changes will be lost Y/N")
        yes_or_no = input(">")
        if yes_or_no.lower() == "y":
            sys.exit("<Game exit")
        elif yes_or_no.lower() == "n":
            continue

    #Saving function    
    elif the_input == ">save":
        json_string = json.dumps(data , indent=4)
        json_saver(json_string=json_string)
        print(">Game saved succesfully")

    #Displays information about character
    elif the_input.startswith(">info"):   
        try:
            the_item = the_input[6:]
            character.item_info(item = the_item)
        except KeyError:
            print("<Please enter a valid item to show info of.")
