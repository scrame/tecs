

#just a wrapper around a dict.
#I do a little extra work to make sure keys are
#always strings and it only accepts ints for values.
class SymbolTable:

    #predefined symbols.
    symbols = {
        "SP" : 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "R0" : 0,
        "R1" : 1,
        "R2" : 2,
        "R3" : 3,
        "R4" : 4,
        "R5" : 5,
        "R6" : 6,
        "R7" : 7,
        "R8" : 8,
        "R9" : 9,
        "R10" : 10,
        "R11" : 11,
        "R12" : 12,
        "R13" : 13,
        "R14" : 14,
        "R15" : 15,
        "SCREEN" : 16384,
        "KBD" : 24576,
        }

    def add_entry(self,symbol,address):
        self.symbols[str(symbol)] = int(address)

    def contains(self,symbol):
        return symbol in self.symbols
    def get_address(self,symbol):
        return self.symbols[str(symbol)]

if(__name__ =='__main__'):
    t = SymbolTable()
    print(t.add_entry(123,123))
    print(t.contains(123))
    print(t.contains('123'))
    print(t.contains("key"))
    print(t.get_address(123))



