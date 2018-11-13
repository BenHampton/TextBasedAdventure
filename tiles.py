import enemies, items

class MapTile:
    def __init__(x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotADirectoryError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y):
        self.item = item
        super().__init__(x,y)

    def add_loot(self, player):
        player.inventory(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EmemeyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.emeny = enemy
        super().__init__(x,y)

    del modify_player(self, player):
    if self.ememy.is_alive():
        the_player.hp = the_player.hp - self.enemy.damage
        print('Ememy does {} damage. You have {} HP remaning.'.formant.(self.ememy.damage, the_player.hp))
