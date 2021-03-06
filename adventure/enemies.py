class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name = "Giant Spider", hp = 5, damage = 2)

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name = "Skeleton", hp = 10, damage = 6)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name = "Ogre", hp = 20, damage = 15)

class Orc(Enemy):
    def __init__(self):
        super().__init__(name = "Orc", hp = 35, damage = 20)
