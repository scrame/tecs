from code import Code
from parser import Parser
from symbol_table import SymbolTable
class Assembler:

    def __init__(self,input_file):
        print("initializing assembler to work on " + input_file)
        self.input_file = input_file
        self.code = Code()
        self.parser = Parser(self.input_file)


    #to implement this, I am going to go with a straight
    #prodcedural implementation. the above functions are the
    #API that is probably needed for the other chapters. 
    
    #Anyway, the parser requires a file for input, and the 
    #advance and has_more_commands are just basic 
    #iterator functions
    #The quickest way to solve this is just implement
    #a counter when the file is initialized.

    def symbol_less_assembly(self):
        #letst iterate!
        while(self.parser.has_more_commands()):
            cmd = self.parser.get_current_command()
            if(self.parser.commands.A_COMMAND==self.parser.command_type()):
                print "A: " + self.parser.symbol()
                #the magic symbol is from here: http://stackoverflow.com/questions/1002116/can-bin-be-overloaded-like-oct-and-hex-in-python-2-6
                self.parser.output.write("0" + '{0:015b}'.format(int(self.parser.symbol()))+"\n")

            elif(self.parser.commands.C_COMMAND==self.parser.command_type()):
                print "C: d=" + str(self.parser.dest()) + " c=" + str(self.parser.comp()) + " j=" + str(self.parser.jump())
                #code emission. should be set to the output_file in the end.
                self.parser.output.write("111" + self.code.comp(self.parser.comp()) + self.code.dest(self.parser.dest()) + self.code.jump(self.parser.jump())+"\n")
            elif(self.parser.commands.L_COMMAND==self.parser.command_type()):
                print "L: " + self.parser.symbol()
            self.parser.advance()



    def two_pass_assembly(self):
        symbol_table = SymbolTable()
        rom_address = 0
        print("starting first pass")
        while(self.parser.has_more_commands()):
            cmd = self.parser.get_current_command()
            if(self.parser.commands.L_COMMAND==self.parser.command_type()):
                print "L: " + self.parser.symbol()
                symbol_table.add_entry(self.parser.symbol(),rom_address)
            else:
                rom_address += 1
            self.parser.advance()
            
        self.parser.reset()


        #the second pass is the same as the first without the print statements, 
        #and without handling (Xxx) syntax

        print("starting second pass")
        while(self.parser.has_more_commands()):
            cmd = self.parser.get_current_command()
            if(self.parser.commands.A_COMMAND==self.parser.command_type()):
                sym = self.parser.symbol()                
                if(sym.isdigit()):
                    val = sym
                else:
                    if(symbol_table.contains(sym)):
                        val = symbol_table.get_address(sym)
                    else:
                        symbol_table.add_entry(sym, rom_address)
                        rom_address += 1
                        val = rom_address
                
                self.parser.output.write("0" + '{0:015b}'.format(int(val))+"\n")

            elif(self.parser.commands.C_COMMAND==self.parser.command_type()):
                self.parser.output.write("111" 
                                         + self.code.comp(self.parser.comp()) 
                                         + self.code.dest(self.parser.dest()) 
                                         + self.code.jump(self.parser.jump())
                                         +"\n")
            self.parser.advance()

