import random
class you():

    def __init__(self):
        self.your_hp = 1000
        self.your_defence = 0

    def targeting_method(self):
        self.your_target = input("Chose your target, {}".format(enemy_list))

    def attack_detrminer(self):
        self.your_attack = input("Chose your attack, a.sword swing, b.roman candel, c.sheild, d.med kit")

    def sowrd_swing(self):
        self.your_target - 50

    def sheild(self):
        self.your_defence + 75

    def med_kit(self):
        self.your_hp + 300

    def roman_candel(self):
        your_target - (random.randint(100-200) + random.randint(100-200))


# Enemy Classes


class crytsal_elemental():
  #Atributes
    hp = 100
    defence = 2
  def bump(self):


  # Ablilitys



class quartz_beast():
  #Atributes
    hp = 350
    defence = 10
    slam = -30
    rock_skin = defence + 15
  # Abilitys

class Earth_bound_rock():
  #Atributes
    hp = 200
    defence =3
    def pelt(self):
      your_hp - 5 * (random.randint(1-5))
    def roll(self):
      your_hp - 10



