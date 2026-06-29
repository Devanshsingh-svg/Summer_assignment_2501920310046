class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty

if __name__ == "__main__":
    inv = Inventory()
    inv.add_item("Apple", 10)
    print(f"Inventory: {inv.items}")
