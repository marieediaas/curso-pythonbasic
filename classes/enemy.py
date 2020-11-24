class Enemy:
    def __init__(self,hp,mp):       #mp magic points
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def get_hp(self):
        return self.hp