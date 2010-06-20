

#Code module from chapter 6 of the elements of computing systems.
class Code:    


    #comp.op should never be null.
    def comp(self,op):
        return self.comp_table[op]

    def dest(self,op):
        if(None == op):
            op = "null"
        return self.dest_table[op]

    def jump(self,op):
        if(None == op):
            op = "null"
        return self.jump_table[op]

    comp_table = {
        #a = 0 -- first digit is zero.
        "0" : "0101010",
        "1" : "0111111",
        "-1" : "0111010",
        "D" : "0001100",
        "A" : "0110000",
        "!D" : "0001101",
        "!A" : "0110001",
        "-D" : "0001111",
        "-A" : "0110011",
        "D+1" : "0011111",
        "A+1" : "0110111",
        "D-1" : "0001110",
        "A-1" : "0110010",
        "D+A" : "0000010",
        "D-A" : "0010011",
        "A-D" : "0000111",
        "D&A" : "0000000",
        "D|A" : "0010101",

        #a = 1, memory instead of address space.
        "M" : "0110000",
        "!M" : "0110001",
        "-M" : "0110011",
        "M+1" : "0110111",
        "M-1" : "0110010",
        "D+M" : "0000010",
        "D-M" : "0010011",
        "M-D" : "0000111",
        "D&M" : "0000000",
        "D|M" : "0010101",
        }


    jump_table = {
        "null" : "000",
        "JGT" : "001",
        "JEQ" : "010",
        "JGE" : "011",
        "JLT" : "100",
        "JNE" : "101",
        "JLE" : "110",
        "JMP" : "111",
        }

    dest_table = {
        "null" : "000",
        "M" : "001",
        "D" : "010",
        "MD" : "011",
        "A" : "100",
        "AM" : "101",
        "AD" : "110",
        "AMD" : "111",
        }

