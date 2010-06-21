from re import sub
from sys import argv
from os import path,mkdir
from enum import Enum
class Parser:

    def __init__(self,input_file):
        print("initializing parser")
        print("loading input")
        self.input_lines = self.__parse_file(input_file)
        print("input lines: " + str(self.input_lines))
        print("creating output")
        self.output = self.__create_output(input_file)


    def __is_comment(self,line):
        if(line.startswith("//")):
            return True
        
    #the current position of the input file
    file_pos = -1
    #returns a list of the lines of the input file
    def __parse_file(self, input_file):
        print("opening: " + str(input_file))
        f = open(input_file)
        self.file_pos = 0
        retval = []
        for line in f.readlines():
            #ignore whitespace
            line = sub("\s+", "", line)
            line = sub("//.*$", "", line)
            if line:
                retval.append(line)
        #So the iteration functions work.
        retval.append(None)
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
    def has_more_commands(self):
        return self.file_pos + 1 < len(self.input_lines)

    #advance: if has_more_commands is true,
    #          read the next command
    def advance(self):
        if(self.has_more_commands()):            
            self.file_pos += 1

    def reset(self):
        self.file_pos = 0

    #support function:
    def get_current_command(self):
        return self.input_lines[self.file_pos]


    commands = Enum('ERROR','A_COMMAND','C_COMMAND','L_COMMAND')

    #command_type: returns the type of command
    #               A_COMMAND,C_COMMAND,L_COMMAND
    def command_type(self):
        cmd = self.get_current_command()

        #A-instruction: @value
        if('@' == cmd[0]):
            return self.commands.A_COMMAND
        #L-instruction starts with (
        elif("(" == cmd[0]):
            return self.commands.L_COMMAND
        #C-instruction otherwise (not a safe assumption)
        else:
            return self.commands.C_COMMAND

    #symbol: returns the symbol or decimal of the current
    #         command, if A_COMMAND or L_COMMAND
    def symbol(self):
        cmd = self.get_current_command()
        #extra muxing since the API required this handle A and L types.
        if(self.commands.A_COMMAND==self.command_type()):
            return cmd[1:len(cmd)]
        elif(self.commands.L_COMMAND==self.command_type()):
            return cmd[1:len(cmd)-1]        
        else:
            return None

    #dest: returns the dest mnemonic for a C_COMMAND
    def dest(self):
        retval = None
        cmd = self.get_current_command()
        idx = cmd.find('=')
        if(-1 != idx):
            retval = cmd[0:idx]
        return retval


    #comp: returns the comp mnemonic for a C_COMMAND
    def comp(self):
        retval = None
        cmd = self.get_current_command()
        idxe = cmd.find('=')
        idxs = cmd.find(';')

        #no jmp
        if(-1 == idxs):
            #no dest
            if(-1 == idxe):
                retval = cmd
            #dest
            else:
                retval = cmd[idxe+1:len(cmd)]
        #jmp
        else:
            #no dest 
            if(-1 == idxe):
                retval = cmd[0:idxs]
            #dest
            else:
                retval = cmd[idxe+1:idxs]
            
        return retval

    #jump: returns the jump mnemonic for a C_COMMAND
    def jump(self):
        retval = None
        cmd = self.get_current_command()
        idx = cmd.find(';')
        if(-1 != idx):
            retval = cmd[idx+1:len(cmd)]
        return retval

