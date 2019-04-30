#import statements here
import random

#Return statements need to be in the following format:
#RETURN type: list
#list[0]: DICT, KEY: action (see Readme), VALUE: Needed Param for method
#list[1]: data

class Robot2():
    def __init__(self):
        pass

    def my_turn(self, stats, team, loc, hp, data):
        #Type your player code here for each turn

        #Random Movement
        x = loc[0] + random.choice([-1,0,1])
        y = loc[0] + random.choice([-1,0,1])
        return [{"move":(x,y)},data]