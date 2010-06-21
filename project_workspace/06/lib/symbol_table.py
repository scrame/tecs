

#just a wrapper around a dict.
#I do a little extra work to make sure keys are
#always strings and it only accepts ints for values.
class SymbolTable:

    def __init__(self):
        self.symbols = {}

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



