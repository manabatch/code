class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, attributes):
        if name in self.symbols:
            print(f"Symbol '{name}' already exists.")
        else:
            self.symbols[name] = attributes
            print(f"Symbol '{name}' inserted.")

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
            return self.symbols[name]
        else:
            return None


def handle_insert():
    name = input("Enter symbol name: ")
    attributes = input("Enter symbol attributes (comma-separated key-value pairs): ")
    attributes = dict(item.split(":") for item in attributes.split(","))
    symbol_table.insert(name, attributes)


def handle_delete():
    name = input("Enter symbol name: ")
    symbol_table.delete(name)


def handle_update():
    name = input("Enter symbol name: ")
    attributes = input("Enter updated symbol attributes (comma-separated key-value pairs): ")
    attributes = dict(item.split(":") for item in attributes.split(","))
    symbol_table.update(name, attributes)


def handle_lookup():
    name = input("Enter symbol name: ")
    attributes = symbol_table.lookup(name)
    if attributes:
        print(f"Symbol '{name}' attributes: {attributes}")
    else:
        print(f"Symbol '{name}' does not exist.")


symbol_table = SymbolTable()

while True:
    print("Symbol Table Operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Lookup")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        handle_insert()
    elif choice == "2":
        handle_delete()
    elif choice == "3":
        handle_update()
    elif choice == "4":
        handle_lookup()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.\n")
    