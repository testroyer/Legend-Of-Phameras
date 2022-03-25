"""
========================================================================
                       LEGEND OF PHAMERAS
                        (Demo / Concept)
                created by testroyer and phonem
                     10 March 2022, 16:47:16
========================================================================
"""

"""
def ToDo():
    -work()
    -delete character()
    -fight()
    -max health
    -a shop catalog would be useful
    -what if it starts without a character ???
    -shop stock ??
    -make one armor equipable.
    -make some changes to the 
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
        player , inventory , player_body = data[0][selected_character] , data[0][selected_character]["Inventory"] ,data[0][selected_character]["Body"]
        
        break
    except KeyError:
        print("<Please enter a valid character name")

#Created for later business. I'm thinking of an error message like "Please write a valid command". Seems it could be done with a for loop checking if the command startswith or just use else.
command_array = [">list" , ">help", "equip", ">unequip" , ">select", ">buy" , ">new character" , ">drop" , ">pick" , ">exit" , ">save" , ">info" , ">health" , ">list body" , ">wear" , ">selfharm"]      

#Saver function made for saving json file. I didn't make a copy of this for the shop.json because it is unnescasary
def json_saver(json_string):                                
    with open("inventory.json" , "w") as f:
            f.write(json_string)
    

character = Character(player = player , player_inventory = inventory , player_body=player_body)
print("<Boot succesfull")

#I believe I can make this one function and then import it
#Checks input every time. I find it bit dumb to make this this way
while True:                 
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

    #It does what it does, lists.
    elif the_input  == ">list":
        if character.character_inventory() != []:            
            character.list_inventory()
        else:
            print("<You have nothing.")

    elif the_input.startswith(">select"):                   #Created for character selection. MAYBE: Write a function that lists characters insted of inventory. 
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

    #Equips an item. I must add a property which makes an item equipable or not.
    elif the_input.startswith(">equip"):             
        try:
            wearable = the_input[7:]
            player_inventory = character.character_inventory()
            if player_inventory[wearable][1] == 2:
                character.equip_item(wearable)
                print(f"<Equipped {wearable}")
            else:
                print("<Please you can't equip this")
        except KeyError:
            print("<Please select a valid wearable")

    #Same thing. Unequips an item. I must add a property which makes an item equipable or not.
    elif the_input.startswith(">unequip"):             
        try:
            wearable = the_input[9:]
            player_body = character.character_body()
            if player_body[wearable][1] == 2:
                character.unequip_item(wearable)
                print(f"<Unequipped {wearable}")
            else:
                print("<Please you can't un-equip this")
        except KeyError:
            print("<Please select a valid wearable")

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
            if character_inventory["Coins"][0] > shop[0][the_item_to_be_bought][0]:
                values = [shop[0][the_item_to_be_bought][1] , shop[0][the_item_to_be_bought][2]]
                character.pick_item(the_item_to_be_bought , values )
                character_inventory["Coins"][0] -= shop[0][the_item_to_be_bought][0]
        except KeyError:
            print("<That item doesn't exists at any one of our shops.")

    #delete character -> If entered nothing next to ">delete character" displays a error message else if there is an entered character name deletes that character. Makes sure to get confirmation.
    elif the_input.startswith(">delete character"):
        character_to_be_deleted = the_input[17:]

    elif the_input.startswith(">new character"):
        new_character = the_input[15:]
        data[0][new_character] = {
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
