import random

class Character():

    #Blank arrays
    player_inventory = []
    player = []
    player_body = []
    attack = 0
    health = 0
    defense = 0
    #init
    def __init__(self , player , player_inventory , player_body) -> None:
        self.player_inventory = player_inventory
        self.player_body = player_body
        self.player = player
        self.attack = player["AttackBase"]
        self.health = player["Health"]

    #Lists every item in inventory
    def list_inventory(self):
        for item in self.player_inventory:
            print(item)

    #Drops an item from inventory. Doesn't work dor "Body"
    def drop_item(self , item):
        self.player_inventory.pop(item)
    
    #Picks an item. Basically Creative Mode. Is not used from now on.
    def pick_item(self , item , value):
        self.player_inventory[item] = value

    #Displays info of the item
    def item_info(self , item):
        print(self.player_inventory[item])

    #displays name. Probably broken
    def character_name(self):
        return print(self.player)
    
    #Function for getting player inventory.
    def character_inventory(self):
        return self.player_inventory

    #Returns player body 
    def character_body(self):
        return self.player_body

    #Hurts himself
    def harm(self , damage):
        self.player["Health"] -= damage

    #Gets health
    def display_health(self):
        return self.player["Health"]

    #Adds an armr to body. Adds the value to the health then removes it from Inventory
    #Will ad the values for wearable, eatable, fightable.
    def equip_armor(self , item):
        self.player_body[item] = self.player_inventory[item]
        defenseCalc = lambda base , value : base + (base * (value / 100))
        self.player["DefenseBase"] = round(defenseCalc(self.player["DefenseBase"], self.player_inventory[item][0]))
        self.player_inventory.pop(item)

    #Adds an armr to body. Adds the value to the health then removes it from Inventory
    def unequip_armor(self , item):
        self.player_inventory[item] = self.player_body[item]
        self.player["DefenseBase"] = 20
        self.player_body.pop(item)
    
    #Lists what is on you
    def list_body(self):
        all_items = []
        for items in self.player_body:
            all_items.append(items)
        return all_items

    def list_coins(self):
        return self.player_inventory["Coins"][0]

    def equip_item(self , item):
        self.player_body[item] = self.player_inventory[item]
        attackBase = self.player["AttackBase"]
        self.player["AttackBase"] = int(round(attackBase + (attackBase * (self.player_inventory[item][0] / 100))))
        self.player_inventory.pop(item)

    def unequip_item(self, item):
        self.player_inventory[item] = self.player_body[item]
        self.player["AttackBase"] = 15
        self.player_body.pop(item)

    def eat(self, food):
        if self.player_inventory[food][1] == 0:
            if self.player["maxHealth"] > self.display_health() + self.player_inventory[food][0]:
                self.player["Health"] += self.player_inventory[food][0]
            elif self.player["maxHealth"] < self.display_health() + self.player_inventory[food][0]:
                self.player["Health"] = self.player["maxHealth"]

            if self.player_inventory[food][2] == 1:
                self.player_inventory.pop(food)
            elif self.player_inventory[food][2] >= 1:
                self.player_inventory[food][2] -= 1
            print(f"Eaten {food}, health is now {self.display_health()}")
        elif self.player_inventory[food][1] != 0:
            print("You cannot eat this.")

    def get_defense(self):
        return self.player["DefenseBase"]
            
    def get_attack(self):
        return self.player["AttackBase"]

    def attack_monster(self, monster):
        monster_defense = monster.defense
        monster.health -= round((((self.attack * ((100 - monster_defense) / 100)) * (random.randint(75, 150))) / 100))