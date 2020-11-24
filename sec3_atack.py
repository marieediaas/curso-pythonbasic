import random


player_hp = 260
enem_atk_low = 60
enem_atk_high = 80

while player_hp > 0:
    damage = random.randrange(enem_atk_low,enem_atk_high)
    player_hp = player_hp - damage

    if player_hp <= 30:
        player_hp= 30
        print("You have low health, so you teleported to the nearest safe place.")
        break

    print("Enemy strikes for ", damage, "points of damage. Current HP is ", player_hp)
