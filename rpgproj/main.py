from classes.game import Person, bcolors

magic = [{"name": "Azarath Metrion Zinthos", "cost": 10, "dmg": 60},
         {"name": "Phasmatos Incendia", "cost": 10, "dmg": 60},
         {"name": "Piertotum Locomotor", "cost": 10, "dmg": 60}
         ]

player = Person(460,65,60,34,magic)

print(player.gen_damage())
print(player.gen_damage())
print(player.gen_damage())