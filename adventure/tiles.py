import enemies, items, actions, world

class MapTile:
    def __init__(x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotADirectoryError()

    def adjacent_moves(self):
        """Return all move actions for adjacent tiles"""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())

        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveWest())

        if world.tile_exists(self.x, self.y - 1)
            moves.append(actions.MoveNorth())

        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveSouth())

    def available_actions(self):
        """Return all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

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

    def available_actions(self):
        if self.enemy.is_alive():
            return [action.Flee(tile = self), actions.Attack(enemy = self.enemy)]
        else:
            return self.adjacent_moves()

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """ You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """
    def modify_player(self, player):
        player.victory = True
