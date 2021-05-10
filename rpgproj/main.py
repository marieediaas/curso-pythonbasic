from classes.game import Person, bcolors

#diccionaries
magic = [{"name": "Azarath Metrion Zinthos", "cost": 10, "dmg": 100},
         {"name": "Phasmatos Incendia", "cost": 12, "dmg": 120},
         {"name": "Piertotum Locomotor", "cost": 10, "dmg": 100}
         ]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 1

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS !" + bcolors.ENDC)

while running:
    print("=====================")
    player.choose_action()
    choice = input("Choose your action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.gen_damage()
        enemy.take_dmg(dmg)
        print("You attacked ", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
        magic_dmg = player.gen_magic_damage(magic_choice)
        spell = player.get_magic_name(magic_choice)
        cost = player.get_magic_cost(magic_choice)

        current_mp = player.get_mp()
        if cost > current_mp:
            print(bcolors.FAIL + "\nYou don't have enough magic points to do that!\n" + bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_dmg(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.gen_damage()
    player.take_dmg(enemy_dmg)
    print("Enemy attacks", enemy_dmg, "points of damage. ")

    print("----------------------------")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("You HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
        running = False