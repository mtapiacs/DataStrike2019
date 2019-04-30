import worldinfo as world
from playerinfo import Player
import bot1
import bot2
import random

class Game():
    def __init__(self):
        self.game_map = world.Map(20, "./maps/tester.txt")
        self.world_objects = self.game_map.get_init_objects()
        self.players = [Player(200, "Red", "Player 1"), Player(200, "Blue", "Player 2")]
        self.game_stats = {}
        self.reset_stats()
        self.update_game_stats(self.world_objects,self.players[1],self.players[0])
        self.team_data = [[],[]]
        #Red is first, blue is second
        self.bot_list = self.determine_colors()
        #self.update_game_stats(world_objects)

    def determine_colors(self):
        num = random.randint(0,2)
        if num == 0:
            bots = [bot1.Robot1(), bot2.Robot2()]
            return bots
        else:
            bots = [bot2.Robot2(), bot1.Robot1()]
            return bots

    def run_round(self):
        #Red Turns
        for o in self.world_objects:
            if o.get_team() == "R":
                my_action = self.bot_list[0].my_turn(self.game_stats, o.get_team(),o.get_location(),o.get_hp(), self.team_data[0])
                o.take_action(my_action)

        #Blue Turns
        for o in self.world_objects:
            if o.get_team() == "B":
                pass

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
        self.game_stats["blue_res"] = self.players[1].get_resources()
        self.game_stats["red_res"] = self.players[0].get_resources()
        


