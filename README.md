# DataStrike2019

Program Flow:
GUI_main.py is initializing a GAME object.
The GAME object will:
    -Create the map from a template
    -add all objects to a list of game objects
    -create two players

Every turn:
    -Call code on each item of object array

Turn Actions:
    build(loc, type)
        Param: loc (x, y), Robot Type
        Return: Boolean    
    move(loc) 
        Param: loc (x, y)
        Return: Boolean
    inspect_location(loc)
        Param: loc (x, y)
        Return: Object Type at Location
    attack(loc)
        Param: loc (x, y)
        Return: 
    cast(loc)
        Param: 
        Return:
    mine(loc)
        Param:
        Return:

Classes:
    -GameObject
        -Unit
        -Resource
    -Player
    -Game
    -Map

TESTING:
    -main.py is used right now for testing without the GUI

TODO:
    -Comment methods
    -Reorganize object creation (get all objects created properly)
