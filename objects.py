import random

class GameObject():
    def __init__(self, t, loc, color):
        self.id = random.randint(100, 1000)
        self.type = t
        self.location = loc
        self.team = color

class Unit(GameObject):
    def __init__(self, c_m, t, loc, color):
        if t == "Base":
            self.can_move = False
        else:
            self.can_move = True
        super(Unit, self).__init__(t, loc, color)

class Resource(GameObject):
    def __init__(self):
        pass

        




