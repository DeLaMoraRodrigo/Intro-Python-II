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

# Declate all items

item = {
    'Sword': Item("Sword", "You find a sword made of iron"),
    'Shield': Item("Shield", "You find a flimsy wooden shield"),
    'Key': Item("Key", "You find a key on the floor... You wonder what it could possibly open")
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

# Fill rooms with items

room['foyer'].add_item(item['Sword'])
room['overlook'].add_item(item['Key'])
room['narrow'].add_item(item['Shield'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Please, enter your name\n")
player = Player(player_name, room['outside'])

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
    player_input = input('Use "w" key to move north, "d" key to move east, "s" key to move south, "a" key to move west, "i" key to open inventory, "o" key to search the room, and "q" to quit game\n')
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
            for index, item in enumerate(player.inventory):
                inv_input = input(f"Do you want to drop {item.name}\nYES/NO\n")
                if inv_input == "NO":
                    continue
                elif inv_input == "YES":
                    print(f"\nYou have dropped your {player.inventory[index].name}\n")
                    player.current_room.add_item(player.inventory[index])
                    player.drop_item(index)
                    break
                else:
                    print("\nPlease enter a valid command\n")
            print("\nYou close your inventory\n")
        else:
            print("\nYour inventory is empty\n")
    elif player_input == "o":
        if len(player.current_room.items) > 0:
            if len(player.current_room.items) > 1:
                print(f"You found {len(player.current_room.items)} items")
            for index, item in enumerate(player.current_room.items):
                print(f"\n{item.description}\n")
                search_input = input(f"Would you like to pick up the {item.name}\nYES/NO\n")
                if search_input == "YES":
                    # print(player.current_room.items[int(index)].name)
                    # print(item.name)
                    print(f"\nYou have picked up the {player.current_room.items[index].name}\n")
                    player.pick_up_item(player.current_room.items[index])
                    player.current_room.remove_item(index)
                    break
                elif search_input == "NO":
                    print("\nYou decide to leave the item\n")
                else:
                    print("\nPlease enter a valid command\n")
        else:
            print("\nYou searched the area and found nothing of interest\n")
    elif player_input == "q":
        running = False
        print("Thank you for playing")
    else:
        print("Please enter a valid command")  
