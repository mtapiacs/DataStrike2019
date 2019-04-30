import random

class GameObject():
    def __init__(self, t, loc, color, icon):
        self.id = random.randint(100, 1000)
        self.type = t
        self.location = loc
        self.team = color
        self.icon = icon

class Unit(GameObject):
    def __init__(self, c_m, t, loc, color, icon):
        if t == "Base":
            self.can_move = False
        else:
            self.can_move = True
        self.move_distance = 1
        super(Unit, self).__init__(t, loc, color, icon)

    def my_location(self):
        return self.location

    def move(self, loc):
        #Checks if various conditions are met
        #Returns True if the move was successful, otherwise returns False
        if (0 <= loc[0] <= 20) and (0 <= loc[1] <= 20):
            if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                if (abs(loc[0] - self.location[0]) <= self.move_distance) and (abs(loc[1] - self.location[1]) <= self.move_distance):
                    self.location = loc
                    return True
        return False

class Resource(GameObject):
    def __init__(self, t, loc, color, icon):
        super(Resource, self).__init__(t, loc, color, icon)

        




