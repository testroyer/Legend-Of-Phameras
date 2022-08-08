import random

class Monster():
    health = None
    attack = None
    defense = None
    loot = None
    monsterDict = {}

    def __init__(self , monsterType : dict):
        self.monsterDict = monsterType
        self.health = self.monsterDict["Health"]
        self.attack = self.monsterDict["Attack"]
        self.defense = self.monsterDict["Defense"]
        self.loot = self.monsterDict["Loot"] 

    def giveLoot(self):
        keys = []
        for loots in self.loot:
            keys.append(loots)
        newLoot = random.choice(keys)
        if newLoot == "Coins":
            return {"Coins" : [random.randint(self.loot["Coins"][0][0] , self.loot["Coins"][0][1]) , 21]} 
        else:
            return {newLoot : [self.loot[newLoot][0] , self.loot[newLoot][1]]}
