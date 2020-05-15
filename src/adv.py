import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside":  Room("Outside Cave Entrance",
                     "You are outside, North of you, the cave mouth beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",["Sword", "Health Potion"]),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",["Torch"]),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Backpack"]),

    "treasure": Room("Treasure Chamber", """You"ve found the long-lost treasure
                     chamber! Gold spills from the walls, waiting to fill your back pack!
                     The only exit is to the south.""", ["Gold!"]),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the "outside" room.
name = str(input("What's your name? "))
player = Player(name, room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn"t allowed.
#
# If the user enters "q", quit the game.
while True:
    if "Gold!" not in player.inventory:
        print(player.current_room.description)
        location = player.current_room
        print(f"There are currently {location.inventory} in the room that you may take.")
        #establish valid commands
        directions = ["n", "s", "e", "w"]
        actions = ["get", "drop"]
        #get current command
        command = str(input("Which way do you want to go? (Enter n, s, e, w. q will quit the game)")).lower()
    if "Gold!" in player.inventory and player.current_room.name == "Treasure Chamber":
        print("You've won! Enter q to quit!")
        command = str(input("Thanks for playing, enter q to quit!")).lower()
        

    if command in directions:
        if command == "n" and hasattr(player.current_room, "n_to"):
            player.current_room = player.current_room.n_to
        elif command == "n" and hasattr(player.current_room, "n_to")!=True:
            print("Can't go that way!")
        elif command == "s" and hasattr(player.current_room, "s_to"):
            player.current_room = player.current_room.s_to
        elif command == "s" and hasattr(player.current_room, "s_to")!=True:
            print("Can't go that way!")
        elif command == "e" and hasattr(player.current_room, "e_to"):
            player.current_room = player.current_room.e_to
        elif command == "e" and hasattr(player.current_room, "e_to")!=True:
            print("Can't go that way!")
        elif command == "w" and hasattr(player.current_room, "w_to"):
            player.current_room = player.current_room.w_to
        elif command == "w" and hasattr(player.current_room, "w_to")!=True:
            print("Can't go that way!")
    elif command.split()[0] in actions:
        item = command.split()[1].capitalize()
        if "get" in command:
            location.inventory.remove(item)
            player.inventory.append(item)
            print(f"You just got {item}")
            print(f"Now you have {player.inventory}")
        if "drop" in command:
            player.inventory.remove(item)
            location.inventory.append(item)
            print(f"You just dropped {item}")
            print(f"Now you have {player.inventory}")
    elif command == "q":
        sys.exit()
    else:
        print("Invalid Command")

        