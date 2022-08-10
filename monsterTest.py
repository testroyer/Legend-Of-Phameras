import json
from classes.monster import Monster
from classes.character import Character
import os




with open(".\Json-Files\monster.json" , "r") as f:             
    data = json.load(f)


with open(".\Json-Files\inventory.json" , "r") as f:             
    char = json.load(f)


monster = Monster(data[0]["Goblin"])

player = char[0]["Larry"]
inventory = char[0]["Larry"]["Inventory"]
player_body = char[0]["Larry"]["Body"]    #I made a body for wearing armor
character = Character(player = player ,player_inventory = inventory , player_body=player_body)


print(monster.attack_player(character))

#C:\Users\alper\Desktop\VS_Code\Python\Legend of Phameras\Legend-Of-Phameras\Json-Files