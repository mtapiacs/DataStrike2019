class Map():
    def __init__(self, side, user_map):
        self.height = side
        self.width = side
        self.layout = []
        self.world_icons = {"Base":"B"}
        self.init_create(user_map)

    def init_create(self, map_path):
        if map_path == "":
            for row in range(self.height):
                temp_list = []
                for col in range(self.width):
                    temp_list.append(None)
                self.layout.append(temp_list)
        else:
            with open(map_path) as maplayout_file:
                for line in maplayout_file:
                    temp_list = []
                    row = line.rstrip().split(" ")
                    for item in row:
                        if item == "--":
                            temp_list.append(None)
                        else:
                            temp_list.append(item)
                    self.layout.append(temp_list)


    def object_lookup(self, object_icon):
        locs = []
        for row in range(len(self.layout)):
            for col in range(len(self.layout[0])):
                locs.append([row, col])

    #Overrides whatever is in that place
    def place_object(self, object_icon, location):
        self.layout[location[0]][location[1]] = object_icon

    def modify_location(self):
        pass

    def print_map(self):
        for row in self.layout:
            for item in row:
                if item == None:
                    print("--", end=' ')
                else:
                    print(item, end=' ')
            print("")


