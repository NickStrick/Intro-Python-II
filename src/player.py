# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currRoom):
        self.room = currRoom
        self.name = name
        self.score = 0
        self.items = []

    def grabItem(self, item):
        if not item.found:
            item.found == True
            self.score += 15
        if self.items == []:
            self.items = [item]
        else:
            self.items = [*self.items, item]

    def dropItem(self, item):
        for i in self.items:
            if item == i:
                self.items.remove(i)

    def changeRoom(self, direction):

        if hasattr(self.room, direction):
            if direction == 'n_to':
                self.room = self.room.n_to
            elif direction == 's_to':
                self.room = self.room.s_to
            elif direction == 'e_to':
                self.room = self.room.e_to
            elif direction == 'w_to':
                self.room = self.room.w_to
            if not self.room.found:
                self.score += 10
                self.room.found = True
        else:
            print('you cant go that way!')
