import random

class GameObject():
    #Type: Base, Soldier, Wizard, Miner, Rock, Tree
    #Location: (x,y)
    #Team: "R", "B", or None
    def __init__(self, t, loc, color, i):
        self.id = random.randint(100, 1000)
        self.type = t
        self.location = loc
        self.team = color
        self.icon = i

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_location(self):
        return self.location

    def get_team(self):
        return self.team

    def get_icon(self):
        return self.icon

class Unit(GameObject):
    def __init__(self, t, loc, color, i):
        super(Unit, self).__init__(t, loc, color, i)
    
class Soldier(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 130
        self.ap = 30
        self.mp = 0
        self.move_max = 1
        super(Soldier, self).__init__(t, loc, color, i)

class Base(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 300
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        super(Base, self).__init__(t, loc, color, i)

class Wizard(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 70
        self.ap = 0
        self.mp = 60
        self.move_max = 0
        super(Wizard, self).__init__(t, loc, color, i)

class Miner(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 40
        self.ap = 0
        self.mp = 0
        self.move_max = 1
        super(Miner, self).__init__(t, loc, color, i)

    def mine(self, loc):
        pass

class Resource(GameObject):
    def __init__(self, t, loc, color, i):
        super(Resource, self).__init__(t, loc, color, i)

class Rock(Resource):
    def __init__(self, t, loc, color, i):
        self.minerals = 400
        super(Rock, self).__init__(t, loc, color, i)

class Tree(Resource):
    def __init__(self, t, loc, color, i):
        self.minerals = 200
        super(Tree, self).__init__(t, loc, color, i)

        




