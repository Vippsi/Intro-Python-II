from room import Room
from player import Player
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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#



# def get_keys(val):
#     for key, value in room.items():
#         if val == value:
#             return key
#         return "Room doesn't exist"

new_player = Player("Jonathan", 'outside')
welcome = "Welcome to the game what would you like to do?    \n 1. M for move, \n 2. I for inventory \n 3. Q for Quit" 
command = input(welcome)

def move_validation(direction):
    try:
        val = getattr(room[new_player.current_room], direction)
        if val != None:
            for key, value in room.items():
                if val == value:
                    new_player.current_room = key
        else:
            pass 
    except AttributeError:
            print("\n =====Invalid Room Choice=====")


# Make a new player object that is currently in the 'outside' room.

while command != 'q':


    while command == 'm':
        
        print(f"\n {new_player.name} is currently in room {room[new_player.current_room].name} \n\n {room[new_player.current_room].description} \n \n") 

        direction = input("Please choose your path... \n N for North \n E for East \n S for South \n W for West \n Q for Quit \n  >>")

        if direction == "n":
            move_validation("n_to")   
            

        elif direction == "e":
            move_validation("e_to")
           

        elif direction == "w":
            move_validation("w_to")
           
        
        elif direction == "s":
            move_validation("s_to")
        
        elif direction == "q":
            exit()
        else: 
            print("Make a better life choice..")




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
