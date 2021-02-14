from room2 import Room
from player2 import Player
from item import Item

# Declare all the rooms

room = {
    'outside cave entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items

item_list = {
    'sword': Item("Sword", "You find a sword made of iron"),
    'shield': Item("Shield", "You find a flimsy wooden shield"),
    'key': Item("Key", "You find a key on the floor... You wonder what it could possibly open")
}


# Link rooms together

room['outside cave entrance'].n_to = room['foyer']
room['foyer'].s_to = room['outside cave entrance']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']

# Fill rooms with items

room['foyer'].add_item(item_list['sword'])
room['grand overlook'].add_item(item_list['key'])
room['narrow passage'].add_item(item_list['shield'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Please, enter your name\n")
player = Player(player_name, room['outside cave entrance'])

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

running = True

while running:
    print(f"============= {player.current_room.name} =============\n")
    player_input = input('Use "w" key to move north, "d" key to move east, "s" key to move south, "a" key to move west, "i" key to open inventory, "o" key to search the room, and "q" to quit game\n').lower()
    notNorth = "There is no path to the north"
    notEast = "There is no path to the east"
    notSouth = "There is no path to the south"
    notWest = "There is no path to the west"
    separator = "==========================================="

    if player_input == "w":
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            print(f"{separator}\n\n{player.current_room.description}\n")
        else:
            print(f"{separator}\n\n{notNorth}\n")
    elif player_input == "d":
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
            print(f"{separator}\n\n{player.current_room.description}\n")
        else:
            print(f"{separator}\n\n{notEast}\n")
    elif player_input == "s":
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
            print(f"{separator}\n\n{player.current_room.description}\n")
        else:
            print(f"{separator}\n\n{notSouth}\n")
    elif player_input == "a":
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
            print(f"{separator}\n\n{player.current_room.description}\n")
        else:
            print(f"{separator}\n\n{notWest}\n")
    elif player_input == "i":
        if len(player.inventory) > 0:
            print("")
            for item in player.inventory:
                print(f"{item.name}")
            inv_input = input("\nWrite the name of the item you would like to drop or write 'CLOSE' to close inventory\n").lower()
            if inv_input == "sword" and player.inventory.__contains__(item_list["sword"]):
                print("\nYou dropped the Sword\n")
                # room[player.current_room.name.lower()].add_item(item_list[inv_input])
                player.current_room.add_item(item_list[inv_input])
                player.drop_item(item_list[inv_input])
            elif inv_input == "shield" and player.inventory.__contains__(item_list["shield"]):
                print("\nYou dropped the Shield\n")
                player.current_room.add_item(item_list[inv_input])
                player.drop_item(item_list[inv_input])
            elif inv_input == "key" and player.inventory.__contains__(item_list["key"]):
                print("\nYou dropped the Key\n")
                player.current_room.add_item(item_list[inv_input])
                player.drop_item(item_list[inv_input])
            elif inv_input == "close":
                print("\nYou close your inventory\n")
            else:
                print("\nPlease enter a valid command\n")
        else:
            print("\nYour inventory is empty\n")
    elif player_input == "o":
        if len(player.current_room.items) > 0:
            print("")
            for item in player.current_room.items:
                print(f"{item.description}: {item.name}")
            search_input = input("\nWrite the name of the item you would like to grab or write 'STOP' to stop searching\n").lower()
            if search_input == "sword" and player.current_room.items.__contains__(item_list["sword"]):
                print("\nYou pick up the sword\n")
                # room[player.current_room.name.lower()].remove_item(item_list[search_input])
                player.current_room.remove_item(item_list[search_input])
                player.pick_up_item(item_list[search_input])
            elif search_input == "shield" and player.current_room.items.__contains__(item_list["shield"]):
                print("\nYou pick up the shield\n")
                player.current_room.remove_item(item_list[search_input])
                player.pick_up_item(item_list[search_input])
            elif search_input == "key" and player.current_room.items.__contains__(item_list["key"]):
                print("\nYou pick up the key\n")
                player.current_room.remove_item(item_list[search_input])
                player.pick_up_item(item_list[search_input])
            elif search_input == "stop":
                print("\nYou decide to stop searching for items\n")
            else:
                print("\nPlease enter a valid command\n")
        else:
            print("\nYou searched the area and found nothing of interest\n")
    elif player_input == "q":
        running = False
        print("\nThank you for playing\n")
    else:
        print("\nPlease enter a valid command\n")  