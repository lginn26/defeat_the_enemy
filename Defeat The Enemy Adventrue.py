import random

class Player:
    def __init__(self):
        self.your_hp = 1000
        self.your_defence = 0

    def targeting_method(self):
        self.your_target = input("Chose your target, {}".format(enemy_list))

    def attack_detrminer(self):
        self.your_attack = input("Chose your attack, a.sword swing, b.roman candel, c.sheild, d.med kit")


    sword_swing = Attack()
    sword_swing.name = "sword_swing"
    sword_swing.damage = your_target - 50

    sheild = Aid()
    sheild.name "sheild"
    sheild.effect = your_defence + 75

    def med_kit(self):
        self.your_hp + 300

    roman_candel =
    def roman_candel(self):
        self.your_target - (random.randint(100-200) + random.randint(100-200))


class Enemy:
    def __init__(self, name, max_hp, defence, attacks, abilities):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attacks = attacks
        self.abilities = abilities


class Aid:
    def __init__(self, name, effect, effectiveness, post_message):
        self.name = name
        self.effect = effect
        self.effectiveness = effectiveness

    def do(self):
        print("{} used {} for {}".format())
        return random.randint(self.effect-self.effectoveness, self.effect+self.variance)

class Attack:
    def __init__(self, name, damage, variance, post_message):
        self.name = name
        self.damage = damage
        self.variance = variance

    def do(self):
        print("{} used {} for {}".format())
        return random.randint(self.damage-self.variance, self.damage+self.variance)


user = Player()
user.your_hp = pass
user.your_defence = pass
user.your_target = pass
user.your_attack = pass
#Attacks/ Abilitys

#--
crystal_elemental = Enemy()
crystal_elemental.name = "Crystal Elemental"
crystal_elemental.max_hp = 100
crystal_elemental.attacks pass
crystal_elemental.abilities pass
#Attacks/ Abilitys

#--
quartz_beast = Enemy()
quartz_beast.name = "Quartz Beast"
quartz_beast.max_hp = 350
quartz_beast.attacks pass
quartz_beast.abilities pass
#Attacks/ Abilitys

#--
earth_bound_rock = Enemy()
earth_bound_rock.name = "Earth Bound Rock"
earth_bound_rock.max_hp = 200
earth_bound_rock.attacks pass
earth_bound_rock.abilities pass
#Attacks/ Abilitys

#--
crystal_ore_bug = Enemy()
crystal_ore_bug.name = "Crystal Ore Bug"
crystal_ore_bug.max_hp = 200
crystal_ore_bug.attacks pass
crystal_ore_bug.abilities pass
#Attacks/ Abilitys

#--




