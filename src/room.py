# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.item_list = []

    def __str__(self):
        return f"{self.name}, {self.description}"

    def add_items(self, item):
        self.item_list.append(item)
    
    def drop_items(self, item):
        self.item_list.remove(item)

    def print_items(self):
        if len(self.item_list) == 0:
            print("No items here for you")
        else: 
            for item in self.item_list:
                print(item)