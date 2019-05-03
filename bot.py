#import statements here
import random

#Return statements need to be in the following format:
#RETURN type: list
#list[0]: DICT, KEY: action (see Readme), VALUE: Needed Param for method
#list[1]: data

class Robot1():

    def __init__(self):
        pass

    def my_turn(self, stats, team, loc, hp, type, data):

        #Type your player code here for each turn
        #RED
        if type == "Wizard":
            return [{"cast":(loc[0]+2,loc[1])}, data]

        if type == "Base":
            return [{"build":("Soldier",(loc[0]+1,loc[1]))}, data]

        if type == "Miner":
            return [{"gather":(loc[0]+1,loc[1])},data]  

        #Random Movement
        x = loc[0] + random.choice([-1,0,1])
        y = loc[1] + random.choice([-1,0,1])
        return [{"move":(x,y)},data]

class Robot2():
    def __init__(self):
        pass

    def my_turn(self, stats, team, loc, hp, type, data):
        #BLUE
        #Type your player code here for each turn
        return [{"cast":(loc[0]-2,loc[1])}, data]
        #return [{"strike":(loc[0]-1,loc[1])}, data]

        #Random Movement
        x = loc[0] + random.choice([-1,0,1])
        y = loc[1] + random.choice([-1,0,1])
        return [{"move":(x,y)},data]
        

        if type == "Soldier" and team == "R":
            return [{"strike":(loc[0]+1,loc[1])}, data]
        elif type == "Soldier" and team == "B":
            #return [{"strike":(loc[0]1,loc[1])}, data]
            return [{"move":(loc[0],loc[1])},data]
        else:
            return [{"move":(loc[0]-1,loc[1])},data]


