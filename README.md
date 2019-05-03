+++------------------DataStrike2019------------------+++

Overview:
The classic Blue and Red factions are warring again! Defeat your enemies 
on the battlefield by gathering resources and building a larger army
than your opponent. You have 300 rounds to try and defeat your opponent. 
At that point, if anyone still has robots left on the battlefield, the tie
breakers will be in the following order: 1.) Team with the most units,
2.) Team with the most resources, 3.) Coin flip. 

How to Start Game:
Execute the python file named GUI_main.py

Where do I modify code?
You are only allowed to modify code in the bot.py. (Robot1 and Robot2)
Every round, each robot will be allowed to return one action. Write
all of your code in the my_turn() function. Do not modify the parameters
of the function, only the internal code. When code is run for a tournament,
it is only your bot.py file that will be submitted, so all other code will
be on the instructor's computer (which means there is no point in modifying it
on your own machine).

What information does my robot have access to?

The parameters for the my_turn() function are as follows:
+-----------------+----------+-------------------------------------------+
|    Parameter    |   Type   |          What does it represent?          |
+-----------------+----------+-------------------------------------------+
| stats           | dict     | various game state information            |
| stats["r_bots"] | dict int | # of red bots on map                      |
| stats["b_bots]  | dict int | # of blue bots on map                     |
| stats["b_res"]  | dict int | # of blue team resources                  |
| stats["r_res"]  | dict int | # of red team resources                   |
| stats["rocks"]  | dict int | # of rocks on map                         |
| stats["trees"]  | dict int | # of trees on map                         |
| stats["round"]  | dict int | current round number                      |
| team            | str      | Team Color, "R" or "B"                    |
| loc             | tuple    | Robot Location, (x, y)                    |
| hp              | int      | Robot health                              |
| type            | str      | Robot type, "Soldier" "Base" etc          |
| data            | list     | Persistent data from one round to another |
+-----------------+----------+-------------------------------------------+

Character Stats

+-----------+-----+----+----+----------+------------+--------+------+
| Character | HP  | AP | MP | Move Max | Attack Max | Vision | Cost |
+-----------+-----+----+----+----------+------------+--------+------+
| Base      | 300 |  0 |  0 |        0 |          0 |     10 | N/A  |
| Soldier   | 130 | 30 |  0 |        1 |          2 |      5 | 40   |
| Miner     |  40 |  0 |  0 |        1 |          0 |      5 | 20   |
| Wizard    |  70 |  0 | 60 |        3 |          3 |      8 | 60   |
+-----------+-----+----+----+----------+------------+--------+------+

What actions do I have access to?

+--------+-------------+---------------------------------+------------------------------------+
| Action | Robot Types |           Description           |           How to Return            |
+--------+-------------+---------------------------------+------------------------------------+
| Move   | S, M, W     | Move robot on map               | return [{"move":(x,y)},data]       |
| Attack | S           | Attack another robot            | return [{"strike":(x,y)},data]     |
| Cast   | W           | Attack another robot            | return [{"cast":(x,y)},data]       |
| Gather | M           | Gather res from trees and rocks | return [{"gather":(x,y)},data]     |
| Build  | B           | Build another robot             | return [{"build":(type,(x,y))},data] |
+--------+-------------+---------------------------------+------------------------------------+

Classes:
    -GameObject
        -Unit
        -Resource
    -Player
    -Game
    -Map

TESTING/DEBUGGING:
    -main.py is used right now for testing without the GUI
    -Look in the gamelog.txt file for object information generated
        every round. This gets overwritten after each game

TODO:
    -comment internal methods
    -Add debug mode to map 
    -Add objects_nearby parameter
