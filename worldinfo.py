import objects


class Map():
    def __init__(self, side, user_map):
        self.init_objects = []
        self.height = side
        self.width = side
        self.layout = []
        self.init_create(user_map)
        self.init_object_creation(self.layout)

    def init_create(self, map_path):
        with open(map_path) as maplayout_file:
            for line in maplayout_file:
                temp_list = []
                row = line.rstrip().split(" ")
                for item in row:
                    # Add in for CLI debugging
                    if item == "--":
                        temp_list.append(None)
                    else:
                        temp_list.append(item)
                self.layout.append(temp_list)

    def init_object_creation(self, lo):
        for row in range(len(lo)):
            for col in range(len(lo[0])):
                # Add objects to be returned
                item = lo[row][col]
                if item == "QU":
                    self.init_objects.append(objects.Rock(
                        "Rock", (col, row), None, "QU"))
                elif item == "TR":
                    self.init_objects.append(objects.Tree(
                        "Tree", (col, row), None, "TR"))
                elif item == "BB":
                    self.init_objects.append(
                        objects.Base("Base", (col, row), "B", "BB"))
                elif item == "BS":
                    self.init_objects.append(objects.Soldier(
                        "Soldier", (col, row), "B", "BS"))
                elif item == "BW":
                    self.init_objects.append(objects.Wizard(
                        "Wizard", (col, row), "B", "BW"))
                elif item == "BM":
                    self.init_objects.append(objects.Miner(
                        "Miner", (col, row), "B", "BM"))
                elif item == "RB":
                    self.init_objects.append(
                        objects.Base("Base", (col, row), "R", "RB"))
                elif item == "RS":
                    self.init_objects.append(objects.Soldier(
                        "Soldier", (col, row), "R", "RS"))
                elif item == "RW":
                    self.init_objects.append(objects.Wizard(
                        "Wizard", (col, row), "R", "RW"))
                elif item == "RM":
                    self.init_objects.append(objects.Miner(
                        "Miner", (col, row), "R", "RM"))

    def get_init_objects(self):
        return self.init_objects

    def object_lookup(self, object_icon):
        locs = []
        for row in range(len(self.layout)):
            for col in range(len(self.layout[0])):
                locs.append([row, col])

    # Overrides whatever is in that place
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
