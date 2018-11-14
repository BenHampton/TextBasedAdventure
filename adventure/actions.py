import Player

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".formant(self.hotkey, self.name)

    class MoveNorth(Action):
        def __init__(self):
            super().__init__(method = Player.move_north, name = "Move North", hotkey="n")

    class MoveEast(Action):
        def __init__(self):
            super().__init__(method = Player.move_east, name = "Move East", hotkey = "e")

    class MoveSouth(Action):
        def __init__(self):
            super().__init__(method = Player.move_south, name = "Move South", hotkey = 's' )

    class MoveWest(Action):
        def __init__(self):
            super().__init__(method = Player.move_west, name = "Move West", hotkey = 'w')

    class ViewInventory(Action):
        """Prints the player's inventory"""
        def __init__(self):
            super().__init__(Player.print_inventory, name = "View Inventory", hotkey = 'i')

    class Attack(Action):
        def __init__(self):
            super().__init__(method = Player.attack, name = "Attack", hotkey = ' a', enemy = enemy)









    
