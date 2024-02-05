from classes.game import Person,bcolors
from classes.magic import Spell

#Create Evil magic
fire = Spell("Fire", 10, 100, "evil")
thunder = Spell("Thunder", 10, 100, "evil")
blizzard = Spell("Blizzard", 10, 100, "evil")
meteor = Spell("Meteor", 20, 200, "evil")
quake = Spell("Quake", 14, 140, "evil")

#Create Good magic
cure = Spell("Cure", 12, 120, "good")
cura = Spell("Cura", 18, 200, "good")

#Instantiate People
player = Person(460,65,60,34,[fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200,65,45,25,[])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==============================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage." )
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n Not enough MP \n" +  bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "good":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), " HP" + bcolors.ENDC)
        elif spell.type == "evil":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" +  spell.name + "deals", str(magic_dmg), "points of damage" +  bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("-----------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) +"/"+ str(enemy.get_max_hp()) +  bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_max_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
        running = False

