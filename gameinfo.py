import worldinfo as world
from playerinfo import Player
import bot1
import random

class Game():
    def __init__(self):
        self.game_map = world.Map(20, "./maps/tester.txt")
        self.world_objects = self.game_map.get_init_objects()
        self.p_red = Player(200, self.game_map.object_lookup("R"), "Red", "Player 1")
        self.p_blue = Player(200, self.game_map.object_lookup("B"), "Blue", "Player 2")
        self.red_robot_count = 2
        self.blue_robot_count = 2
        self.game_stats = {}
        self.reset_stats()
        self.update_game_stats(self.world_objects,self.p_blue,self.p_red)
        #self.update_game_stats(world_objects)


    def create_new_world_object(self, object_icon, location):
        pass

    def playerTurn(self, player):
        return player.my_turn()

    def print_game_map(self):
        return self.game_map.print_map()

    def get_game_objects(self):
        return self.world_objects

    def get_game_stats(self):
        return self.game_stats

    def reset_stats(self):
        self.game_stats["red_bots"] = 0
        self.game_stats["blue_bots"] = 0
        self.game_stats["blue_res"] = 0
        self.game_stats["red_res"] = 0
        self.game_stats["rocks"] = 0
        self.game_stats["trees"] = 0
        self.game_stats["round"] = 100

    #Run after each round
    def update_game_stats(self, wo, blue_p, red_p):
        for o in wo:
            if o.get_team() == "R":
                self.game_stats["red_bots"] += 1
            elif o.get_team() == "B":
                self.game_stats["blue_bots"] += 1
            elif o.get_type() == "Rock":
                self.game_stats["rocks"] += 1
            elif o.get_type() == "Tree":
                self.game_stats["trees"] += 1
        self.game_stats["blue_res"] = self.p_blue.get_resources()
        self.game_stats["red_res"] = self.p_red.get_resources()
        


