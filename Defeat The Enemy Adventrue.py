import random

class Player:
    def __init__(self):
        self.your_hp = 1000
        self.your_defence = 0

    def targeting_method(self):
        self.your_target = input("Chose your target, {}".format(enemy_list))

    def attack_detrminer(self):
        self.your_attack = input("Chose your attack, a.sword swing, b.roman candel, c.sheild, d.med kit")

    def sword_swing(self):
        self.your_target - 50

    def sheild(self):
        self.your_defence + 75

    def med_kit(self):
        self.your_hp + 300

    def roman_candel(self):
        self.your_target - (random.randint(100-200) + random.randint(100-200))


class Enemy:
    def __init__(self, name, max_hp, attacks, abilities):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attacks = attacks
        self.abilities = abilities


class Attack:
    def __init__(self, name, damage, variance, post_message):
        self.name = name
        self.damage = damage
        self.variance = variance

    def do(self):
        print("{} used {} for {}".format())
        return random.randint(self.damage-self.variance, self.damage+self.variance)


user = Player()
