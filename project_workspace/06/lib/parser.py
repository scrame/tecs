
class Parser:
    def __init__(self,input_file):
        print("initializing parser")
        self.__parse_file(input_file)

    def __parse_file(self, input_file):
        print("opening: " + str(input_file))
        f = open(input_file)
        lines = f.readlines()

