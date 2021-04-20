from classes.game import Person, bcolors

#diccionaries
magic = [{"name": "Azarath Metrion Zinthos", "cost": 10, "dmg": 60},
         {"name": "Phasmatos Incendia", "cost": 10, "dmg": 80},
         {"name": "Piertotum Locomotor", "cost": 10, "dmg": 60}
         ]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 1
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS !" + bcolors.ENDC)

