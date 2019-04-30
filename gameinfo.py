import worldinfo as world
from playerinfo import Player
import bot1
import random

class Game():
    def __init__(self):
        self.game_map = world.Map(20, "./maps/tester.txt")
        self.world_objects = {}
        self.p1 = Player(200, self.game_map.object_lookup("R"), "Red", "Player 1")
        self.p2 = Player(200, self.game_map.object_lookup("B"), "Blue", "Player 2")
        self.red_robot_count = 2
        self.blue_robot_count = 2

    #Won't work because place_object is changed
    def create_new_world_object(self, object_icon, location):
        r_num = -1
        while r_num == -1 or r_num in self.world_objects:
            r_num = random.randint(100, 1000)
        self.world_objects[r_num] = [object_icon, location]
        self.game_map.place_object(object_icon, location)
        print(self.world_objects) #DEBUG

    def playerTurn(self, player):
        return player.my_turn()

    def print_game_map(self):
        return self.game_map.print_map()

