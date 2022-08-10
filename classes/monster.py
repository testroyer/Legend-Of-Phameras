import random
from classes.character import Character

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

    def get_loot(self):
        keys = []
        for loots in self.loot:
            keys.append(loots)
        newLoot = random.choice(keys)
        if newLoot == "Coins":
            return {"Coins" : [random.randint(self.loot["Coins"][0][0] , self.loot["Coins"][0][1]) , 21]} 
        else:
            return {newLoot : [self.loot[newLoot][0] , self.loot[newLoot][1]]}

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health
        
    def get_defense(self):
        return self.defense

    def attack_player(self, player:Character) -> int:
        player_defense = player.get_defense()
        return round((self.attack * ((100 - player_defense) / 100)) * ((random.randint(95, 105)) / 100 ))
