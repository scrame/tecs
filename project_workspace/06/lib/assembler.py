from code import Code
from parser import Parser
from symbol_table import SymbolTable
class Assembler:

    def __init__(self,input_file):
        print("initializing assembler to work on " + input_file)
        self.input_file = input_file


    #to implement this, I am going to go with a straight
    #prodcedural implementation. the above functions are the
    #API that is probably needed for the other chapters. 
    
    #Anyway, the parser requires a file for input, and the 
    #advance and has_more_commands are just basic 
    #iterator functions
    #The quickest way to solve this is just implement
    #a counter when the file is initialized.

    def symbol_less_assembly(self):
        self.code = Code()
        self.parser = Parser(self.input_file)
        self.symbol_table = SymbolTable()
        #letst iterate!
        while(parser.has_more_commands()):
            cmd = parser.get_current_command()
            if(self.commands.A_COMMAND==parser.command_type()):
                print "A: " + parser.symbol()
                #the magic symbol is from here: http://stackoverflow.com/questions/1002116/can-bin-be-overloaded-like-oct-and-hex-in-python-2-6
                self.output.write("0" + '{0:015b}'.format(int(parser.symbol()))+"\n")

            elif(self.commands.C_COMMAND==parser.command_type()):
                print "C: d=" + str(parser.dest()) + " c=" + str(parser.comp()) + " j=" + str(parser.jump())
                #code emission. should be set to the output_file in the end.
                self.output.write("111" + code.comp(parser.comp()) + code.dest(parser.dest()) + code.jump(parser.jump())+"\n")
            elif(self.commands.L_COMMAND==parser.command_type()):
                print "L: " + parser.symbol()
            parser.advance()



    def two_pass_assembly(self):
        self.code = Code()
        self.parser = Parser(self.input_file)
        self.symbol_table = SymbolTable()
