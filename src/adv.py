from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('candle'), Item('rusty nail')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('candy')]),

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


def adventure():

    pName = input("Input your name: ")
    hero = Player(pName, room['outside'])
    print(f'welcome {hero.name}')

    # gameStart = True

    # for r in room:
    #     # print(r)
    #     if hero.room == r:
    #         currRoom = room[r]
    print(f'\nlocation: {hero.room.name} \n   {hero.room.description}\n')
    print('===========================\n')
    action = input("Enter a Direction.\nor 'q' to quit: ")
    print('===========================\n')

    while not action == 'q':
        # print(hero.room.items)
        # for r in room:
        #     # print(r)
        #     if hero.room == r:
        #         currRoom = room[r]

        def setDirection(direction):
            if hasattr(hero.room, direction):
                if direction == 'n_to':
                    hero.room = hero.room.n_to
                elif direction == 's_to':
                    hero.room = hero.room.s_to
                elif direction == 'e_to':
                    hero.room = hero.room.e_to
                elif direction == 'w_to':
                    hero.room = hero.room.w_to
            else:
                print('you cant go that way!')

        direction = ''
        if action == 'north':
            direction = 'n_to'
        elif action == 'south':
            direction = 's_to'
        elif action == 'east':
            direction = 'e_to'
        elif action == 'west':
            direction = 'w_to'

        elif action == 'items':
            currItems = hero.items
            print('your items:')
            for i in currItems:
                print(f'    {i.name}')

        elif 'get' in action:
            actArr = action.split(' ', 1)
            if len(actArr) == 2:
                roomItems = hero.room.items
                for i in roomItems:
                    if i.name == actArr[1]:
                        print(f'you picked up {i.name}!')
                        hero.grabItem(i)
                        hero.room.removeItem(i)
            else:
                print('you must type a item to get it!')

        elif 'drop' in action:
            actArr = action.split(' ', 1)
            if len(actArr) == 2:
                currItems = hero.items
                for i in currItems:
                    if i.name == actArr[1]:
                        print(f'you dropped {i.name}!')
                        hero.dropItem(i)
                        hero.room.setItem(i)

            else:
                print('you must type a item to get it!')

        elif action == 'look':
            roomItems = hero.room.items
            print('room items:')
            for i in roomItems:
                print(f'    {i.name}')
        elif action == 'q':
            print('you quit!!!')
        else:
            print('sorry, i didnt understand that!')
        if not direction == '':
            setDirection(direction)

        # for r in room:
        #     if hero.room == r:
        #         currRoom = room[r]

        print(f'\nlocation: {hero.room.name} \n\n   {hero.room.description}\n')
        print('===========================\n')
        action = input("What will you do?.\nor 'q' to quit: ")
        print('===========================\n')


if __name__ == '__main__':
    adventure()
# finished on day 1 mvp
