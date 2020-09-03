from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


items = {
    'coins': Item("Coins", "These shinny morsels are worth a pretty penny"),
    'sword': Item("Sword", "This sword has the reach of the gods, swing wisely"),
    'broom': Item("Broom", "Once for sweeping, now for...")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to rooms
room['outside'].add_items(items['coins'])
room['foyer'].add_items(items['broom'])
room['foyer'].add_items(items['coins'])
room['overlook'].add_items(items['sword'])
room['treasure'].add_items(items['coins'])
room['treasure'].add_items(items['coins'])
room['treasure'].add_items(items['coins'])



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player("Jonathan", room['outside'])
welcome = "Welcome to the game what would you like to do?    \n 1. M for move, \n 2. I for inventory \n 3. Q for Quit \n >>" 
current_command = input(welcome)
linebreak = "+++===+++===+++===+++"


while current_command != 'q':

    while current_command == 'm':
        
        print(f"\n\n {player} \n")
        print("Upon entering the room you notice... ") 
        player.room.print_items()
        print(f"{linebreak} \n")

        direction = input("Please choose your path... \n N for North \n E for East \n S for South \n W for West \n Q for Quit \n I for Inventory (to add/remove from your inventory, open inventory and follow prompts) \n >> ")

        direction_command = f"{direction.lower()}_to"

        if direction not in ['n', 'w', 's', 'e', 'q', 'c', 'i']:
            print("invalid command choice")
        elif direction == "q":
            exit()
        elif direction == "c":
            player.room.print_items()
        elif direction == "i":
            current_command = "i"
        else:
            player.move(direction_command)

    while current_command == 'i':
        item_info = "Would you like to take or drop an item? \n\n Type 'get' followed by the item name to add an item to your inventory or 'drop' followed by the item name to remove an item. \n\n You can type 'go back' to go back to the menu"

        print(linebreak)

        print("\n These are the items in the room: \n")
        player.room.print_items()

        print(linebreak)

        print("\nThese are the items in your inventory \n")
        player.print_items()



        print(linebreak)
        command_input = input(item_info)
        action = command_input.split()[0].lower()
        item = command_input.split()[1].lower()


    
        if action == "go" and item == "back":
            current_command = input(welcome)

        elif action == "get":
            for i in player.room.item_list:
                if i.name.lower() == item:
                    player.take_item(i)
                    player.room.drop_items(i)

        elif action == "drop":
            for i in player.items:
                if i.name.lower() == item:
                    player.drop_item(i)
                    player.room.add_items(i)
        

        elif action != "get" or action != "drop" or action != "back":
            command_input = input("Please enter a valid command " + item_info)


exit()