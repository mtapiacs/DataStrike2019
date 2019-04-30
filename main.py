#Current Step:
#Creating game objects and seeing if they are set with the correct properties

#import classes
from gameinfo import Game


#create game instance
campaign = Game()
campaign.print_game_map()
campaign.create_new_world_object("RS", [1, 10])
campaign.print_game_map()
