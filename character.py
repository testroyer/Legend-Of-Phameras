#https://www.w3schools.com/python/default.asp

class Character():
    player_inventory = []
    player = []
    def __init__(self , player , player_inventory) -> None:
        self.player_inventory = player_inventory
        self.player = player

    def list_inventory(self):
        for item in self.player_inventory:
            print(item)

    def drop_item(self , item):
        self.player_inventory.pop(item)
    
    def pick_item(self , item , value):
        self.player_inventory[item] = value

    def item_info(self , item):
        print(self.player_inventory[item])

    def character_name(self):
        return print(self.player_inventory)
    
    def character_inventory(self):
        return self.player_inventory

    def harm(self , damage):
        self.player["Health"] -= damage

    def display_health(self):
        return self.player["Health"]
