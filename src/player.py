# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def pick_up_item(self, item):
        self.inventory.append(item)

    def drop_item(self, index):
        for i, item in enumerate(self.inventory):
            if index == i and item:
                # print(self.inventory[index].name)
                del self.inventory[index]
                break