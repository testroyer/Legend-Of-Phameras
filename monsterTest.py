import json
from classes.monster import Monster
import os




with open(".\Json-Files\monster.json" , "r") as f:             
    data = json.load(f)

monster = Monster(data[0]["Goblin"])

print(monster.giveLoot())

#C:\Users\alper\Desktop\VS_Code\Python\Legend of Phameras\Legend-Of-Phameras\Json-Files