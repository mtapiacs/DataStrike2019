class Player():
    def __init__(self, r, startp, color, name):
        self.resources = r
        self.start_positions = startp
        self.game_color = color
        self.team_name = name

    def player_turn(self):
        #In PROGRESS
        pass

    def create_soldier(self):
        #IN PROGRESS
        pass

    def get_resources(self):
        return self.resources

    def get_color(self):
        return self.game_color

    def get_name(self):
        return self.team_name