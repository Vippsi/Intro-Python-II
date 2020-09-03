# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f"{self.name} is currently in room {self.room}"

    def take_item(self, item):
        self.items.append(item)
        return f"You have picked up {item}"
    
    def drop_item(self, item):
        self.items.remove(item)
        return f"You have dropped {item}"

    def move(self, direction):
        val = getattr(self.room, direction)
        if val != None:
            self.room = getattr(self.room, direction)

    def print_items(self):
        if len(self.items) == 0:
            print("No items here for you")
        else: 
            for item in self.items:
                print(item)