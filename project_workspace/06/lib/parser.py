from sys import argv
from os import path,mkdir
class Parser:
    def __init__(self,input_file):
        print("initializing parser")
        print("loading input")
        self.input_lines = self.__parse_file(input_file)
        print("creating output")
        self.output = self.__create_output(input_file)


        
    #the current position of the input file
    file_pos = -1
    #returns a list of the lines of the input file
    def __parse_file(self, input_file):
        print("opening: " + str(input_file))
        f = open(input_file)
        self.file_pos = 0
        retval = []
        for line in f.readlines():
            line = line.rstrip()
            if line:
                retval.append(line)
        return retval

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

    #to track the current command
    current_command = None

    #has_more_commands: hasNext() on the input
    def __has_more_commands(self):
#        print("has_more_commands")
        return self.file_pos + 1 < len(self.input_lines)

    #advance: if has_more_commands is true,
    #          read the next command
    def __advance(self):
#        print("advance")
        if(self.__has_more_commands()):            
            self.file_pos += 1

    #support function:
    def __get_current_command(self):
#        print("SUPPORT: get_current_command")
        if(self.__has_more_commands() ):
            next_cmd = self.input_lines[self.file_pos]
            return next_cmd
        return None


    #Fake Enum:
    ERROR = -1
    A_COMMAND = 0
    C_COMMAND = 1
    #Still first pass havn't implemented
    #symbols and loops
    #L_COMMAND = 2


    #command_type: returns the type of command
    #               A_COMMAND,C_COMMAND,L_COMMAND
    def __command_type(self):
#        print("command_type")
        cmd = self.__get_current_command()
#        print "char[0]: " + str(cmd[0])

        #A-instruction: @value
        if('@' == cmd[0]):
            return "A_COMMAND: " + cmd
        return "ERROR: " + str(cmd) + " not yet handled"

    #symbol: returns the symbol or decimal of the current
    #         command, if A_COMMAND or L_COMMAND
    def __symbol(self):
        print("symbol")

    #dest: returns the dest mnemonic for a C_COMMAND
    def __dest(self):
        print("dest")

    #comp: returns the comp mnemonic for a C_COMMAND
    def __comp(self):
        print("comp")

    #jump: returns the jump mnemonic for a C_COMMAND
    def __jump(self):
        print("jump")

    #to implement this, I am going to go with a straight
    #prodcedural implementation. the above functions are the
    #API that is probably needed for the other chapters. 
    
    #Anyway, the parser requires a file for input, and the 
    #advance and has_more_commands are just basic 
    #iterator functions
    #The quickest way to solve this is just implement
    #a counter when the file is initialized.

    #calls the commands in serial,
    #basic test shouldn't fail
    def test(self):
        self.__has_more_commands()
        self.__advance()
        self.__command_type()
        self.__symbol()
        self.__dest()
        self.__comp()
        self.__jump()
        #letst iterate!
        while(self.__has_more_commands()):
#            print self.__get_current_command()
            print self.__command_type()
            self.__advance()
        


if __name__ == "__main__":
    print("running main for " + str(argv[0]))


