#Current Step:
#Creating game objects and seeing if they are set with the correct properties

#import classes
from gameinfo import Game


#create game instance
campaign = Game()
campaign.print_game_map()
print(campaign.get_game_objects())
print(campaign.get_game_stats())
