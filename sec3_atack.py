import random

class Enemy:
    hp = 200
    def __init__(self, atkl, atkh):
        self.atk_low = atkl
        self.atk_high = atkh

    def getAtack(self):
        print("Atack is ", self.atk_low)

    def getHP(self):
        print("Hp is ", self.hp)

enemy1 = Enemy(40,49)
enemy1.getAtack()
enemy1.getHP()
print("")
enemy2 = Enemy(75,90)
enemy2.getAtack()
enemy2.getHP()


'''
player_hp = 260
enem_atk_low = 60
enem_atk_high = 80

while player_hp > 0:
    damage = random.randrange(enem_atk_low,enem_atk_high)
    player_hp = player_hp - damage

    if player_hp <= 30:
        player_hp= 30

    print("Enemy strikes for ", damage, "points of damage. Current HP is ", player_hp)

    if player_hp > 30:
        continue

    print("You have low health, so you teleported to the nearest safe place.")
    break
'''