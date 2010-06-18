from os import path,mkdir
class Parser:
    def __init__(self,input_file):
        print("initializing parser")
        print("loading input")
        input = self.__parse_file(input_file)
        print("creating output")
        output = self.__create_output(input_file)


        

    #returns a list of the lines of the input file
    def __parse_file(self, input_file):
        print("opening: " + str(input_file))
        f = open(input_file)
        return f.readlines()

    #returns a writeable output handle to "build"
    #todo: y'know.
    def __create_output(self, input_file_name):
        build = "build"
        file_name = path.basename(input_file_name)
        base = path.splitext(file_name)[0]
        print "base: " + base
        if(not(path.exists(build))):
            mkdir(build)
        return open(build+"/"+base+".hack","w")


    #the following are the methods
    #suggested by the text.

    #has_more_commands: hasNext() on the input
    def has_more_commands(self):
        print("has_more_commands")

    #advance: if has_more_commands is true,
    #          read the next command
    def advance(self):
        print("advance")

    #command_type: returns the type of command
    #               A_COMMAND,C_COMMAND,L_COMMAND
    def command_type(self):
        print("command_type")

    #symbol: returns the symbol or decimal of the current
    #         command, if A_COMMAND or L_COMMAND
    def symbol(self):
        print("symbol")

    #dest: returns the dest mnemonic for a C_COMMAND
    def dest(self):
        print("dest")

    #comp: returns the comp mnemonic for a C_COMMAND
    def comp(self):
        print("comp")

    #jump: returns the jump mnemonic for a C_COMMAND
    def jump(self):
        print("jump")

