class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, attributes):
        if name in self.symbols:
            print(f"Symbol '{name}' already exists.")
        else:
            self.symbols[name] = attributes

    def delete(self, name):
        if name in self.symbols:
            del self.symbols[name]
            print(f"Symbol '{name}' deleted.")
        else:
            print(f"Symbol '{name}' does not exist.")

    def update(self, name, attributes):
        if name in self.symbols:
            self.symbols[name] = attributes
            print(f"Symbol '{name}' updated.")
        else:
            print(f"Symbol '{name}' does not exist.")

    def lookup(self, name):
        if name in self.symbols:
            print(name,'->',self.symbols[name])
        else:
            print("error")

# Example usage
symbol_table = SymbolTable()

# Insertion
print("insert to the symbol table")
while(1):
    i ,type= input().split()
    if(i == 'end'):
        break
    symbol_table.insert(i, {'type': type, 'id': id(i)})
    print("inserted")

# Lookup
symbol_table.lookup('i')  # {'type': 'int', 'scope': 'global'}
symbol_table.lookup('y')  # {'type': 'float', 'scope': 'local'}
symbol_table.lookup('z')  # {'type': 'string', 'scope': 'global'}
symbol_table.lookup('a')  # None

# Updation
symbol_table.update('y', {'type': 'double', 'id': id('y')})
symbol_table.lookup('y')

# Deletion
symbol_table.delete('i')
symbol_table.lookup('i') # None