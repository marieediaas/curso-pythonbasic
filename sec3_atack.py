import random

class Enemy:
    atk_low = 60
    atk_high = 80

    def getAtack(self):
        print(self.atk_low)

enemy1 = Enemy()
enemy1.getAtack()


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