from room import Room
from player import Player
from item import Item
from item import LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [LightSource('candle', 'dim, but hot'), Item('rusty nail', 'gross')], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item('candy', 'a delicious sugary treat'), LightSource('oil lamp', 'its a very old lamp')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item('rock', 'a rock the size of your palm')], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item('rag', 'just a dirty piece of cloth')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item('coins', 'some gold pieces found beside a chest')]),

    'cavern':   Room("Cavern Floor", """There is a tall cliff above you, 
you see two very dark hallways going east and west. 
To your north is a small crawl hole, you hear a noise coming from it, 
but its too muffled to make out what it is""",
                     [Item('empty bottle', 'Its an empty glass bottle with a cork holding it shut,  maybe you can put something in it')]),

    'deadend':  Room("Dead End", """Just rocky cave walls in all directions, 
only way out is the way you came in """,
                     [Item('pickaxe', 'a used pickaxe, still in good condition')]),

    'furnace':  Room("Smelting Room", """Theres a furnace in the center of the room, 
its on but has almost no fuel. To the west theres a locked wodden door""",
                     ),
    'cave':     Room("Cave passage", """looks like there was a cave collapse, a mound of rocks block your way. 
there is a broken minecart in the center with coal spilling out""",
                     [Item('coal', 'some freshly mined coal')])

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['cavern']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['cavern'].n_to = room['furnace']
room['cavern'].e_to = room['deadend']
room['cavern'].w_to = room['cave']
room['cavern'].s_to = room['overlook']
room['deadend'].w_to = room['cavern']
room['cave'].e_to = room['cavern']
room['furnace'].s_to = room['cavern']
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

    def hasLight(room, currItems):
        roomItems = room.items
        light = False
        if room.is_light:
            light = True
        for i in currItems:
            if isinstance(i, LightSource):
                light = True
        if not light:
            for i in roomItems:
                if isinstance(i, LightSource):
                    light = True
        return light

    isLit = hasLight(hero.room, hero.items)

    if isLit:
        print(
            f'\nlocation: {hero.room.name} \n\n   {hero.room.description}\n')
    else:
        print('It\'s pitch black!')
    print('===========================\n')
    action = input("What will you do?.\nor 'q' to quit: ")
    print('===========================\n')

    while not action == 'q':

        direction = ''
        actArr = action.lower().strip().split(' ', 1)

        # handles direction commands
        if actArr[0] == 'go':
            if actArr[1] == 'north':
                direction = 'n_to'
            elif actArr[1] == 'south':
                direction = 's_to'
            elif actArr[1] == 'east':
                direction = 'e_to'
            elif actArr[1] == 'west':
                direction = 'w_to'
        elif actArr[0] == 'north':
            direction = 'n_to'
        elif actArr[0] == 'south':
            direction = 's_to'
        elif actArr[0] == 'east':
            direction = 'e_to'
        elif actArr[0] == 'west':
            direction = 'w_to'

        # handles item viewing commands
        elif action == 'items' or action == 'inventory' or action == 'i':
            currItems = hero.items
            print('your items:')
            for i in currItems:
                print(f'    {i.name}')
        elif action == 'look' and isLit:
            roomItems = hero.room.items
            print('room items:')
            for i in roomItems:
                print(f'    {i.name}')
        elif actArr[0] == 'look' and isLit:
            if len(actArr) == 2:
                currItems = hero.items
                roomItems = hero.room.items
                found = False
                for i in currItems:
                    if i.name == actArr[1]:
                        found = True
                        i.look()
                        break
                if not found:
                    for i in roomItems:
                        if i.name == actArr[1]:
                            i.look()
                            break
        elif 'look' in action and not isLit:
            print('You cant do that, its too dark!')

        # handles player actions
        elif actArr[0] == 'get' or actArr[0] == 'take' or actArr[0] == 'grab':
            if not isLit:
                print('Good luck finding that in the dark!')
            else:
                if len(actArr) == 2:
                    roomItems = hero.room.items
                    for i in roomItems:
                        if i.name == actArr[1]:
                            i.onTake()
                            hero.grabItem(i)
                            hero.room.removeItem(i)
                            break
                else:
                    print('you must type a item to get it!')

        elif 'drop' in action:
            if len(actArr) == 2:
                currItems = hero.items
                for i in currItems:
                    if i.name == actArr[1]:
                        i.onDrop()
                        hero.dropItem(i)
                        hero.room.setItem(i)
                        break

            else:
                print('you must type a item to drop it!')

        elif actArr[0] == 'score':
            print(f'Current Score: {hero.score}')

        # empy/quit commands
        else:
            print('sorry, i didnt understand that!')
        if not direction == '':
            hero.changeRoom(direction)

        #
        # checks if room is lit

        isLit = hasLight(hero.room, hero.items)

        if isLit:
            print(
                f'\nlocation: {hero.room.name} \n\n   {hero.room.description}\n')
        else:
            print('It\'s pitch black!')
        print('===========================\n')
        action = input("What will you do?.\nor 'q' to quit: ")
        print('===========================\n')
        if action == 'q':
            print(f'Final Score: {hero.score}\n')


if __name__ == '__main__':
    adventure()
