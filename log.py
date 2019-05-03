class Log():
    def __init__(self, filen):
        self.filename = filen
        self.initialize_file()

    def initialize_file(self):
        with open(self.filename, "w") as myFile:
            myFile.write("DATASTRIKE2019")

    def add_to_file(self, line):
        with open(self.filename, "a") as myFile:
            myFile.write(line)       

