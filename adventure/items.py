class Item:
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name = "Gold", description = "A round coin with {} stamped on the front.".format(str(self.amt)), value = self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name = "Rock", description = "A fist-size rock, suitable for bludgeonig.", value = 0, damage = 5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name = "Dagger", description = "small rusty dagger, good for close encounters.", value = 3, damage = 8)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name = "Sword", description = "One-Handed Sword, Great for attacking larger enimies.", value = 10, damage = 15)
