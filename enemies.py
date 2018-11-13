class Emeny:
    def __init__(self, name, hp, damage)
    self.name = name
    self.hp = hp
    self.damage = damage

    def is_alive(self):
        return self.hp > 0

class GaintSpider(Enemy):
    def __init__(self):
        super()__init__(name = "Giant Spider", hp = 5, damage = 2)

class Skeleton(Emeny):
    def __init__(self):
        super()__init__(name = "Skeleton", hp = 10, damage = 6)

class Oger(Emeny):
    def __init__(self):
        super()__init__(name = "Oger", hp = 20, damage = 15)

class Orc(Emeny):
    def __init__(self):
        super()__init__(name = "Orc", hp = 35, damage = 20)
