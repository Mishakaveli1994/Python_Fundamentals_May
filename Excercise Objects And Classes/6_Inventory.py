class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.capacity = capacity
    def add_item(self, item):
        if self.capacity > 0:
            self.capacity -= 1
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        result = ''
        result += f"Items: {', '.join(self.items)}.\n"
        result += f"Capacity left: {self.capacity}"
        return result


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
