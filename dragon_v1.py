from random import randint


class Dragon:
    def __init__(self, name, position_x, position_y):
        self.name = name
        self.positionX = position_x
        self.positionY = position_y
        self.health = randint(50, 100)
        self.texture = 'img/dragon/alive.png'
        self.status = 'alive'
        self.gold_loot = randint(1, 100)

    def set_position(self, position_x, position_y):
        self.positionX = position_x
        self.positionY = position_y
        return f'({self.positionX}, {self.positionY})'

    def move(self, move_x, move_y):
        self.positionX += move_x
        self.positionY += move_y
        return f'({self.positionX}, {self.positionY})'

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.status = 'dead'
            self.texture = 'img/dragon/dead.png'
            return f'Dragon {self.name} is dead. \n' \
                   f'Loot: {self.gold_loot} gold \n' \
                   f'Corpse position: ({self.positionX}, {self.positionY})'
        else:
            return f'Dragon took {damage} hp damage'

    def attack(self) -> int:  # noqa
        return randint(5, 20)

    def stats(self):
        return f'Name: {self.name} \n' \
               f'Hp: {self.health} \n' \
               f'Position: ({self.positionX}, {self.positionY}) \n' \
               f'Status: {self.status}'


smok = Dragon('Wawelski', 50, 120)
smok.set_position(10, 20)
smok.move(-10, 20)
smok.move(-10+15, 0)
smok.move(15, -5)
smok.move(0, 5)
smok.attack()
smok.take_damage(10)
smok.take_damage(5)
smok.take_damage(3)
smok.take_damage(2)
smok.take_damage(15)
smok.take_damage(25)
smok.take_damage(75)
smok.stats()
