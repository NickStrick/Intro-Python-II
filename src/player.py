# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currRoom):
        self.room = currRoom
        self.name = name
        self.score = 0
        self.items = []

    def grabItem(self, item):
        if self.items == []:
            self.items = [item]
        else:
            self.items = [*self.items, item]

    def dropItem(self, item):
        for i in self.items:
            if item == i:
                self.items.remove(i)

            else:
                print('item isnt in list!!!')
